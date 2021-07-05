from pathlib import Path
from typing import Dict

import yaml

from .schema_utils import models

SCHEMA_FILE = Path(__file__).parent / "db_schema.yaml"
RESOURCES_FILE = Path(__file__).parent / "resources.yml"
RESOURCES_EXTRA_FILE = Path(__file__).parent / "resources_extra.yml"


with SCHEMA_FILE.open("r") as f:
    schema_dict = yaml.safe_load(f)
    meta_nodes_dict_raw: Dict[str, models.RawMetaNode] = schema_dict[
        "meta_nodes"
    ]
    meta_rels_dict_raw: Dict[str, models.RawMetaRel] = schema_dict["meta_rels"]

with RESOURCES_FILE.open("r") as f:
    resources_dict_raw: models.RawResources = yaml.safe_load(f)

with RESOURCES_EXTRA_FILE.open("r") as f:
    resources_extra_dict: models.RawResourcesExtra = yaml.safe_load(f)
