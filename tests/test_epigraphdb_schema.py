from typing import Dict

from ..epigraphdb_schema import meta_nodes_dict, meta_rels_dict
from ..schema_utils import models


def test_nodes_dict_type():
    assert isinstance(meta_nodes_dict, Dict)
    for key, value in meta_nodes_dict.items():
        assert isinstance(value, models.DataDictNode)


def test_rels_dict_type():
    assert isinstance(meta_rels_dict, Dict)
    for key, value in meta_rels_dict.items():
        assert isinstance(value, models.DataDictRel)
