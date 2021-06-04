from typing import Dict

# HACK: neural is using pydantic 1.7 whereas others using 1.8
from pydantic import create_model_from_typeddict  # type: ignore

from ..epigraphdb_schema import (
    DataDictNode,
    DataDictRel,
    RawMetaNode,
    RawMetaRel,
    meta_nodes_dict,
    meta_nodes_dict_raw,
    meta_rels_dict,
    meta_rels_dict_raw,
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
