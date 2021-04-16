from typing import Dict

from pydantic import create_model_from_typeddict

from ..epigraphdb_schema import (
    DataDictNode,
    DataDictRel,
    SchemaExtra,
    meta_nodes_dict,
    meta_rels_dict,
    schema_extra_dict,
)


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
