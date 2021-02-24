from pprint import pprint

import pytest

from epigraphdb_common_utils.epigraphdb_data_dicts import (
    DataDictNodeEntity,
    DataDictRelEntity,
    PopulatedProperty,
    meta_nodes_dict_sanitised,
    meta_nodes_properties_sanitised,
    meta_rels_dict_sanitised,
    meta_rels_properties_sanitised,
)


@pytest.mark.parametrize(
    "prop_data", [meta_nodes_properties_sanitised, meta_rels_properties_sanitised]
)
def test_properties(prop_data):
    assert isinstance(prop_data, dict)
    for key, value in prop_data.items():
        if isinstance(value, dict):
            for value_key, value_value in value.items():
                assert PopulatedProperty(**value_value)


def test_node_dict():
    for key, value in meta_nodes_dict_sanitised.items():
        print(key)
        pprint(value)
        assert DataDictNodeEntity(**value)


def test_rel_dict():
    for key, value in meta_rels_dict_sanitised.items():
        print(key)
        pprint(value)
        assert DataDictRelEntity(**value)
