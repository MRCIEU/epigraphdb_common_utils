import copy
from typing import Any, Dict, List, Optional, Union, cast

from . import models

# list of properties that should not render, as they are not normal properties
META_REL_PROP_BLACKLIST = ["source", "target"]
NEO4J_TYPE_MAPPING = {"string": "str", "float": "float", "integer": "int"}


def sanitise_properties(
    entity_data: Union[models.RawMetaNode, models.RawMetaRel],
    blacklist: List[str] = [],
) -> Dict[str, models.EntityProperty]:
    def _format_type(
        property: Union[models.RawPropertyArray, models.RawPropertyScalar]
    ) -> str:
        # array
        if property["type"] == "array":
            array_property = cast(models.RawPropertyArray, property)
            item_type = NEO4J_TYPE_MAPPING[array_property["items"]["type"]]
            res = f"List[{item_type}]"
            return res
        # scalar
        else:
            scalar_property = cast(models.RawPropertyScalar, property)
            res = NEO4J_TYPE_MAPPING[scalar_property["type"]]
            return res

    def _check_required(prop_name: str, required_props: List[str]):
        return prop_name in required_props

    property_data = entity_data["properties"]
    required_props = entity_data["required"]
    property_docs = {
        key: models.EntityProperty(
            doc=value["doc"],
            type=_format_type(value),
            required=_check_required(key, required_props),
        )
        for key, value in property_data.items()
        if key not in blacklist
    }
    return property_docs


def sanitise_meta_nodes(
    meta_nodes_dict_raw: Dict[str, Any],
    resources_dict: Dict[str, Dict[str, models.Resource]],
) -> Dict[str, models.DataDictNode]:
    def _process(key, entity, resources_dict) -> models.DataDictNode:
        id_field = entity["meta"]["_id"]
        name_field = entity["meta"]["_name"]
        api_resources = collect_resources(
            key, "meta_node", resources_dict["api"]
        )
        web_resources = collect_resources(
            key, "meta_node", resources_dict["web"]
        )
        rpkg_resources = collect_resources(
            key, "meta_node", resources_dict["rpkg"]
        )
        resources = models.MetaEntityResources(
            api=api_resources, web=web_resources, rpkg=rpkg_resources
        )
        res = models.DataDictNode(
            id=id_field,
            name=name_field,
            doc=entity["doc"],
            properties=property_docs[key],
            resources=resources,
        )
        return res

    property_docs = {
        meta_entity_name: sanitise_properties(meta_entity_data)
        for meta_entity_name, meta_entity_data in meta_nodes_dict_raw.items()
    }

    res = {
        key: _process(key, value, resources_dict)
        for key, value in meta_nodes_dict_raw.items()
    }
    return res


def sanitise_meta_rels(
    meta_rels_dict_raw: Dict[str, Any],
    resources_dict: Dict[str, Dict[str, models.Resource]],
) -> Dict[str, models.DataDictRel]:
    def _process(key, entity, resources_dict) -> models.DataDictRel:
        source_field = entity["properties"]["source"]["type"]
        target_field = entity["properties"]["target"]["type"]
        api_resources = collect_resources(
            key, "meta_rel", resources_dict["api"]
        )
        web_resources = collect_resources(
            key, "meta_rel", resources_dict["web"]
        )
        rpkg_resources = collect_resources(
            key, "meta_rel", resources_dict["rpkg"]
        )
        resources = models.MetaEntityResources(
            api=api_resources, web=web_resources, rpkg=rpkg_resources
        )
        res = models.DataDictRel(
            source=source_field,
            target=target_field,
            doc=entity["doc"],
            properties=property_docs[key],
            resources=resources,
        )
        return res

    property_docs = {
        meta_entity_name: sanitise_properties(
            meta_entity_data, blacklist=META_REL_PROP_BLACKLIST
        )
        for meta_entity_name, meta_entity_data in meta_rels_dict_raw.items()
    }

    res = {
        key: _process(key, value, resources_dict)
        for key, value in meta_rels_dict_raw.items()
    }
    return res


def collect_doc(
    entity: Union[models.DataDictNode, models.DataDictRel]
) -> Dict[str, str]:
    res = {key: value.doc for key, value in entity.properties.items()}
    return res


def process_resources(
    resources_dict_raw: Dict[str, Any]
) -> Dict[str, Dict[str, models.Resource]]:
    api_resources = {
        key: process_api_resource(value)
        for key, value in resources_dict_raw["api"].items()
    }
    web_resources = {
        key: process_web_resource(value, api_resources)
        for key, value in resources_dict_raw["web"].items()
    }
    rpkg_resources = {
        key: process_rpkg_resource(value, api_resources)
        for key, value in resources_dict_raw["rpkg"].items()
    }
    res = {"api": api_resources, "web": web_resources, "rpkg": rpkg_resources}
    return res


def process_api_resource(item: Dict) -> models.Resource:
    url = api_url_formatter(item["uri"])
    assoc_ents = item["assoc_ents"] if "assoc_ents" in item.keys() else None
    triples = set(item["triples"]) if "triples" in item.keys() else None
    res = models.Resource(
        label=item["name"],
        uri=item["uri"],
        url=url,
        meta_nodes=item["meta_nodes"],
        meta_rels=item["meta_rels"],
        query_ents=item["query_ents"],
        assoc_ents=assoc_ents,
        triples=triples,
    )
    return res


def process_web_resource(
    item: Dict, api_resources: Dict[str, models.Resource]
) -> models.Resource:
    url = web_url_formatter(item["uri"])
    if "parent" in item.keys() and item["parent"] in api_resources.keys():
        res = copy.deepcopy(api_resources[item["parent"]])
        res.label = item["name"]
        res.uri = item["uri"]
        res.url = url
    else:
        assoc_ents = (
            item["assoc_ents"] if "assoc_ents" in item.keys() else None
        )
        res = models.Resource(
            label=item["name"],
            uri=item["uri"],
            url=url,
            meta_nodes=item["meta_nodes"],
            meta_rels=item["meta_rels"],
            query_ents=item["query_ents"],
            assoc_ents=assoc_ents,
        )
    return res


def process_rpkg_resource(
    item: Dict, api_resources: Dict[str, models.Resource]
) -> models.Resource:
    url = rpkg_url_formatter(item["uri"])
    if "parent" in item.keys() and item["parent"] in api_resources.keys():
        res = copy.deepcopy(api_resources[item["parent"]])
        res.label = item["uri"]
        res.uri = item["uri"]
        res.url = url
    else:
        assoc_ents = (
            item["assoc_ents"] if "assoc_ents" in item.keys() else None
        )
        res = models.Resource(
            label=item["uri"],
            uri=item["uri"],
            url=url,
            meta_nodes=item["meta_nodes"],
            meta_rels=item["meta_rels"],
            query_ents=item["query_ents"],
            assoc_ents=assoc_ents,
        )
    return res


def api_url_formatter(uri: str) -> str:
    url_template = "https://docs.epigraphdb.org/api/api-endpoints/#{uri}"
    return url_template.format(uri=uri)


def web_url_formatter(uri: str) -> str:
    # url_template = "https://epigraphdb.org/{uri}"
    # this should be enough for a web instance?
    url_template = "/{uri}"
    return url_template.format(uri=uri)


def rpkg_url_formatter(uri: str) -> str:
    url_template = "https://mrcieu.github.io/epigraphdb-r/reference/{uri}.html"
    return url_template.format(uri=uri)


def collect_resources(
    entity: str, entity_type: str, resources: Dict[str, models.Resource]
) -> Optional[Dict[str, models.LinkedResource]]:
    linked_resources = []
    for key, item in resources.items():
        meta_node_p = entity_type == "meta_node" and entity in item.meta_nodes
        meta_rel_p = entity_type == "meta_rel" and entity in item.meta_rels
        if meta_node_p or meta_rel_p:
            queriable = True if entity in item.query_ents else False
            linked_item = models.LinkedResource(
                queriable=queriable,
            )
            linked_resources.append({"key": key, "item": linked_item})
    if len(linked_resources) == 0:
        return None
    else:
        res = {_["key"]: _["item"] for _ in linked_resources}
        return res
