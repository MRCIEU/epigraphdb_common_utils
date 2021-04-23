from typing import Dict

from pydantic import create_model_from_typeddict

from ..epigraphdb_schema import (
    DataDictNode,
    DataDictRel,
    RawMetaNode,
    RawMetaRel,
    SchemaExtra,
    meta_nodes_dict,
    meta_nodes_dict_raw,
    meta_rels_dict,
    meta_rels_dict_raw,
    schema_extra_dict,
)


def test_meta_nodes_dict_raw():
    Model = create_model_from_typeddict(RawMetaNode)
    for key, value in meta_nodes_dict_raw.items():
        assert Model(**value)


def test_meta_rels_dict_raw():
    Model = create_model_from_typeddict(RawMetaRel)
    for key, value in meta_rels_dict_raw.items():
        assert Model(**value)


def test_nodes_dict_type():
    assert isinstance(meta_nodes_dict, Dict)
    for key, value in meta_nodes_dict.items():
        assert isinstance(value, DataDictNode)


def test_rels_dict_type():
    assert isinstance(meta_rels_dict, Dict)
    for key, value in meta_rels_dict.items():
        assert isinstance(value, DataDictRel)


def test_schema_extra_type():
    SchemaExtraModel = create_model_from_typeddict(SchemaExtra)
    assert SchemaExtraModel(**schema_extra_dict)
