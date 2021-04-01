from typing import Any, Dict, List, Union

from .models import DataDictNode, DataDictRel, EntityProperty

# list of properties that should not render, as they are not normal properties
META_REL_PROP_BLACKLIST = ["source", "target"]
NEO4J_TYPE_MAPPING = {"string": "str", "float": "float", "integer": "int"}


def sanitise_properties(
    property_data: Dict[str, Dict], blacklist: List[str] = []
) -> Dict[str, EntityProperty]:
    def _format_type(value: Dict) -> str:
        # array
        if value["type"] == "array":
            item_type = NEO4J_TYPE_MAPPING[value["items"]["type"]]
            res = f"List[{item_type}]"
            return res
        # scalar
        else:
            res = NEO4J_TYPE_MAPPING[value["type"]]
            return res

    property_docs = {
        key: EntityProperty(doc=value["doc"], type=_format_type(value))
        for key, value in property_data.items()
        if key not in blacklist
    }
    return property_docs


def sanitise_meta_nodes(
    meta_nodes_dict_raw: Dict[str, Any]
) -> Dict[str, DataDictNode]:
    def _process(key, entity) -> DataDictNode:
        id_field = entity["meta"]["_id"]
        name_field = entity["meta"]["_name"]
        res = DataDictNode(
            id=id_field,
            name=name_field,
            doc=entity["doc"],
            properties=property_docs[key],
        )
        return res

    property_docs = {
        key: sanitise_properties(value["properties"])
        for key, value in meta_nodes_dict_raw.items()
    }

    res = {
        key: _process(key, value) for key, value in meta_nodes_dict_raw.items()
    }
    return res


def sanitise_meta_rels(meta_rels_dict_raw) -> Dict[str, DataDictRel]:
    def _process(key, entity) -> DataDictRel:
        source_field = entity["properties"]["source"]["type"]
        target_field = entity["properties"]["target"]["type"]
        res = DataDictRel(
            source=source_field,
            target=target_field,
            doc=entity["doc"],
            properties=property_docs[key],
        )
        return res

    property_docs = {
        key: sanitise_properties(
            value["properties"], blacklist=META_REL_PROP_BLACKLIST
        )
        for key, value in meta_rels_dict_raw.items()
    }

    res = {
        key: _process(key, value) for key, value in meta_rels_dict_raw.items()
    }
    return res


def collect_doc(entity: Union[DataDictNode, DataDictRel]) -> Dict[str, str]:
    res = {key: value.doc for key, value in entity.properties.items()}
    return res
