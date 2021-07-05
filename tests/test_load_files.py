from pydantic import create_model_from_typeddict

from ..load_files import (
    meta_nodes_dict_raw,
    meta_rels_dict_raw,
    resources_dict_raw,
    resources_extra_dict,
)
from ..schema_utils import models


def test_meta_nodes_dict_raw():
    Model = create_model_from_typeddict(models.RawMetaNode)
    for key, value in meta_nodes_dict_raw.items():
        assert Model(**value)


def test_meta_rels_dict_raw():
    Model = create_model_from_typeddict(models.RawMetaRel)
    for key, value in meta_rels_dict_raw.items():
        assert Model(**value)


def test_resources_dict_raw():
    Model = create_model_from_typeddict(models.RawResources)
    assert Model(**resources_dict_raw)


def test_resources_extra_dict():
    Model = create_model_from_typeddict(models.RawResourcesExtra)
    assert Model(**resources_extra_dict)
