from typing import Dict

from .load_files import resources_extra_dict  # noqa
from .load_files import (
    meta_nodes_dict_raw,
    meta_rels_dict_raw,
    resources_dict_raw,
)
from .schema_utils import models, resources, schema

resources_dict: models.EpigraphdbPlatformResources = (
    resources.process_resources(resources_dict_raw)
)

meta_nodes_dict: Dict[str, models.DataDictNode] = schema.sanitise_meta_nodes(
    meta_nodes_dict_raw, resources_dict
)
meta_rels_dict: Dict[str, models.DataDictRel] = schema.sanitise_meta_rels(
    meta_rels_dict_raw, resources_dict
)

meta_nodes_property_docs: Dict[str, Dict[str, str]] = {
    meta_node_name: schema.collect_doc(meta_node_value)
    for meta_node_name, meta_node_value in meta_nodes_dict.items()
}

meta_rels_property_docs: Dict[str, Dict[str, str]] = {
    meta_rel_name: schema.collect_doc(meta_rel_value)
    for meta_rel_name, meta_rel_value in meta_rels_dict.items()
}
