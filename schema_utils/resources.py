import copy
from typing import Any, Dict

from . import models


def process_resources(
    resources_dict_raw: Dict[str, Any]
) -> models.EpigraphdbPlatformResources:
    api_resources: Dict[str, models.Resource] = {
        key: process_api_resource(value)
        for key, value in resources_dict_raw["api"].items()
    }
    web_resources: Dict[str, models.Resource] = {
        key: process_web_resource(value, api_resources)
        for key, value in resources_dict_raw["web"].items()
    }
    rpkg_resources: Dict[str, models.Resource] = {
        key: process_rpkg_resource(value, api_resources)
        for key, value in resources_dict_raw["rpkg"].items()
    }
    res: models.EpigraphdbPlatformResources = {
        "api": api_resources,
        "web": web_resources,
        "rpkg": rpkg_resources,
    }
    return res


def process_api_resource(item: Dict) -> models.Resource:
    url = api_url_formatter(item["uri"])
    triples = set(item["triples"]) if "triples" in item.keys() else None
    res = models.Resource(
        label=item["name"],
        uri=item["uri"],
        url=url,
        meta_nodes=item["meta_nodes"],
        meta_rels=item["meta_rels"],
        query_ents=item["query_ents"],
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
        res = models.Resource(
            label=item["name"],
            uri=item["uri"],
            url=url,
            meta_nodes=item["meta_nodes"],
            meta_rels=item["meta_rels"],
            query_ents=item["query_ents"],
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
        res = models.Resource(
            label=item["uri"],
            uri=item["uri"],
            url=url,
            meta_nodes=item["meta_nodes"],
            meta_rels=item["meta_rels"],
            query_ents=item["query_ents"],
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
