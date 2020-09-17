from itertools import chain
from pathlib import Path
from typing import Dict, List, Optional, Union

import yaml
from pydantic import BaseModel

META_NODES_FILE = Path(__file__).parent / "data-dict-meta-nodes.yml"
META_RELS_FILE = Path(__file__).parent / "data-dict-meta-rels.yml"


class PopulatedProperty(BaseModel):
    "The property field populated."
    doc: str


class DataDictNodeEntity(BaseModel):
    "Meta node entity as specified by the data dict."
    id: Optional[str]
    name: Optional[str]
    doc: Optional[str]
    properties: List[Union[str, Dict[str, PopulatedProperty]]]


class DataDictRelEntity(BaseModel):
    "Meta relationship entity as specified by the data dict."
    source: str
    target: str
    doc: Optional[str]
    properties: Optional[List[Union[str, Dict[str, PopulatedProperty]]]]


with META_NODES_FILE.open("r") as f:
    meta_nodes_dict = yaml.safe_load(f)

with META_RELS_FILE.open("r") as f:
    meta_rels_dict = yaml.safe_load(f)


def get_doc(item: Union[str, Dict]) -> Optional[Dict]:
    if isinstance(item, str):
        return {item: None}
    elif isinstance(item, dict):
        res_dict = list(item.items())[0]
        if "doc" in res_dict[1].keys():
            return {res_dict[0]: res_dict[1]["doc"]}
        else:
            return res_dict[0]


def get_property_docs(
    property_data: List[Union[str, Dict]]
) -> Optional[Dict[str, Optional[str]]]:

    if property_data is None:
        return None
    else:
        dict_list = [get_doc(item) for item in property_data]
        res: Dict[str, Optional[str]] = dict(
            chain.from_iterable(_.items())  # type: ignore
            for _ in dict_list
            if _ is not None
        )
        return res


meta_nodes_property_docs = {
    key: get_property_docs(value["properties"])
    for key, value in meta_nodes_dict.items()
}

meta_rels_property_docs = {
    key: get_property_docs(value["properties"])
    for key, value in meta_rels_dict.items()
}
