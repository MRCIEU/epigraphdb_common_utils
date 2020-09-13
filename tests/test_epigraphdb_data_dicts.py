import pytest

from epigraphdb_common_utils.epigraphdb_data_dicts import (
    meta_nodes_docs,
    meta_rels_docs,
)


@pytest.mark.parametrize("docs_data", [meta_nodes_docs, meta_rels_docs])
def test_docs(docs_data):
    assert isinstance(docs_data, dict)
    for key, value in docs_data.items():
        if isinstance(value, dict):
            for value_key, value_value in value.items():
                assert isinstance(value_value, str) or value_value is None
