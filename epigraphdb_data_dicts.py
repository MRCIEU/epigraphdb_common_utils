from pathlib import Path
from typing import Any, Dict, List

import yaml
from pydantic import BaseModel

SCHEMA_FILE = Path(__file__).parent / "db_schema.yaml"
# list of properties that should not render, as they are not normal properties
META_REL_PROP_BLACKLIST = ["source", "target"]


class PopulatedProperty(BaseModel):
    "The property field populated."
    doc: str


class DataDictNodeEntity(BaseModel):
    "Meta node entity as specified by the data dict."
    id: str
    name: str
    doc: str
    properties: Dict[str, PopulatedProperty]


class DataDictRelEntity(BaseModel):
    "Meta relationship entity as specified by the data dict."
    source: str
    target: str
    doc: str
    properties: Dict[str, PopulatedProperty]


def sanitise_properties(
    property_data: Dict[str, Dict], blacklist: List[str] = []
) -> Dict[str, Dict[str, Any]]:
    property_docs = {
        key: {"doc": value["doc"]}
        for key, value in property_data.items()
        if key not in blacklist
    }
    return property_docs


def sanitise_meta_nodes_dict(meta_nodes_dict, property_docs):
    """Sanitise data dictionary for proper formatting
    """

    def _render(key, entity):
        id_field = entity["meta"]["_id"]
        name_field = entity["meta"]["_name"]
        res = {
            "id": id_field,
            "name": name_field,
            "doc": entity["doc"],
            "properties": property_docs[key],
        }
        return res

    res = {key: _render(key, value) for key, value in meta_nodes_dict.items()}
    return res


def sanitise_meta_rels_dict(meta_rels_dict, property_docs):
    """Sanitise data dictionary for proper formatting
    """

    def _render(key, entity):
        source_field = entity["properties"]["source"]["type"]
        target_field = entity["properties"]["target"]["type"]
        res = {
            "source": source_field,
            "target": target_field,
            "doc": entity["doc"],
            "properties": property_docs[key],
        }
        return res

    res = {key: _render(key, value) for key, value in meta_rels_dict.items()}
    return res


with SCHEMA_FILE.open("r") as f:
    schema_dict = yaml.safe_load(f)
    meta_nodes_dict = schema_dict["meta_nodes"]
    meta_rels_dict = schema_dict["meta_rels"]


# For displaying property docs at data table
meta_nodes_properties_sanitised = {
    key: sanitise_properties(value["properties"])
    for key, value in meta_nodes_dict.items()
}
meta_rels_properties_sanitised = {
    key: sanitise_properties(
        value["properties"], blacklist=META_REL_PROP_BLACKLIST
    )
    for key, value in meta_rels_dict.items()
}
# For displaying schema docs at docs site
meta_nodes_dict_sanitised = sanitise_meta_nodes_dict(
    meta_nodes_dict, meta_nodes_properties_sanitised
)
meta_rels_dict_sanitised = sanitise_meta_rels_dict(
    meta_rels_dict, meta_rels_properties_sanitised
)
