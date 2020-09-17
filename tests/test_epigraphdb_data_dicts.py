import pytest

from epigraphdb_common_utils.epigraphdb_data_dicts import (
    DataDictNodeEntity,
    DataDictRelEntity,
    meta_nodes_dict,
    meta_nodes_property_docs,
    meta_rels_dict,
    meta_rels_property_docs,
)


@pytest.mark.parametrize(
    "docs_data", [meta_nodes_property_docs, meta_rels_property_docs]
)
def test_docs(docs_data):
    assert isinstance(docs_data, dict)
    for key, value in docs_data.items():
        if isinstance(value, dict):
            for value_key, value_value in value.items():
                assert isinstance(value_value, str) or value_value is None


def test_node_dict():
    for key, value in meta_nodes_dict.items():
        print(key)
        assert DataDictNodeEntity(**value)


def test_rel_dict():
    for key, value in meta_rels_dict.items():
        print(key)
        assert DataDictRelEntity(**value)
