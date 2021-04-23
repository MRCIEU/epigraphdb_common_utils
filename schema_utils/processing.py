from typing import Any, Dict, List, Union, cast

from .models import (
    DataDictNode,
    DataDictRel,
    EntityProperty,
    RawMetaNode,
    RawMetaRel,
    RawPropertyArray,
    RawPropertyScalar,
)

# list of properties that should not render, as they are not normal properties
META_REL_PROP_BLACKLIST = ["source", "target"]
NEO4J_TYPE_MAPPING = {"string": "str", "float": "float", "integer": "int"}


def sanitise_properties(
    entity_data: Union[RawMetaNode, RawMetaRel], blacklist: List[str] = []
) -> Dict[str, EntityProperty]:
    def _format_type(
        property: Union[RawPropertyArray, RawPropertyScalar]
    ) -> str:
        # array
        if property["type"] == "array":
            array_property = cast(RawPropertyArray, property)
            item_type = NEO4J_TYPE_MAPPING[array_property["items"]["type"]]
            res = f"List[{item_type}]"
            return res
        # scalar
        else:
            scalar_property = cast(RawPropertyScalar, property)
            res = NEO4J_TYPE_MAPPING[scalar_property["type"]]
            return res

    def _check_required(prop_name: str, required_props: List[str]):
        return prop_name in required_props

    property_data = entity_data["properties"]
    required_props = entity_data["required"]
    property_docs = {
        key: EntityProperty(
            doc=value["doc"],
            type=_format_type(value),
            required=_check_required(key, required_props),
        )
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
        meta_entity_name: sanitise_properties(meta_entity_data)
        for meta_entity_name, meta_entity_data in meta_nodes_dict_raw.items()
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
        meta_entity_name: sanitise_properties(
            meta_entity_data, blacklist=META_REL_PROP_BLACKLIST
        )
        for meta_entity_name, meta_entity_data in meta_rels_dict_raw.items()
    }

    res = {
        key: _process(key, value) for key, value in meta_rels_dict_raw.items()
    }
    return res


def collect_doc(entity: Union[DataDictNode, DataDictRel]) -> Dict[str, str]:
    res = {key: value.doc for key, value in entity.properties.items()}
    return res
