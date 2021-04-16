from typing import Dict

from ..epigraphdb_schema import (
    DataDictNode,
    DataDictRel,
    meta_nodes_dict,
    meta_rels_dict,
)


def test_nodes_dict_type():
    assert isinstance(meta_nodes_dict, Dict)
    for key, value in meta_nodes_dict.items():
        assert isinstance(value, DataDictNode)


def test_rels_dict_type():
    assert isinstance(meta_rels_dict, Dict)
    for key, value in meta_rels_dict.items():
        assert isinstance(value, DataDictRel)
