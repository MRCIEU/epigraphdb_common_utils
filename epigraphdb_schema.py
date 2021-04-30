from pathlib import Path
from typing import Any, Dict

import yaml

from .schema_utils.models import (
    DataDictNode,
    DataDictRel,
    RawMetaNode,
    RawMetaRel,
)
from .schema_utils.processing import (
    collect_doc,
    process_resources,
    sanitise_meta_nodes,
    sanitise_meta_rels,
)

SCHEMA_FILE = Path(__file__).parent / "db_schema.yaml"
RESOURCES_FILE = Path(__file__).parent / "resources.yml"


with SCHEMA_FILE.open("r") as f:
    schema_dict = yaml.safe_load(f)
    meta_nodes_dict_raw: Dict[str, RawMetaNode] = schema_dict["meta_nodes"]
    meta_rels_dict_raw: Dict[str, RawMetaRel] = schema_dict["meta_rels"]

with RESOURCES_FILE.open("r") as f:
    resources_dict_raw: Dict[str, Any] = yaml.safe_load(f)

resources_dict = process_resources(resources_dict_raw)

meta_nodes_dict: Dict[str, DataDictNode] = sanitise_meta_nodes(
    meta_nodes_dict_raw, resources_dict
)
meta_rels_dict: Dict[str, DataDictRel] = sanitise_meta_rels(
    meta_rels_dict_raw, resources_dict
)

meta_nodes_property_docs: Dict[str, Dict[str, str]] = {
    meta_node_name: collect_doc(meta_node_value)
    for meta_node_name, meta_node_value in meta_nodes_dict.items()
}

meta_rels_property_docs: Dict[str, Dict[str, str]] = {
    meta_rel_name: collect_doc(meta_rel_value)
    for meta_rel_name, meta_rel_value in meta_rels_dict.items()
}
