from pydantic import create_model_from_typeddict

from ..epigraphdb_schema import meta_nodes_dict_raw, meta_rels_dict_raw
from ..schema_utils import models


def test_meta_nodes_dict_raw():
    Model = create_model_from_typeddict(models.RawMetaNode)
    for key, value in meta_nodes_dict_raw.items():
        assert Model(**value)


def test_meta_rels_dict_raw():
    Model = create_model_from_typeddict(models.RawMetaRel)
    for key, value in meta_rels_dict_raw.items():
        assert Model(**value)
