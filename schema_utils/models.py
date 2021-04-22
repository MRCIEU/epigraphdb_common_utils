from dataclasses import dataclass
from typing import Dict, List, Union

from typing_extensions import Literal, TypedDict


@dataclass
class EntityProperty:
    "The property fields for a meta entity."
    doc: str
    type: str
    required: bool


@dataclass
class DataDictNode:
    "Meta node entity as specified by the data dict."
    id: str
    name: str
    doc: str
    properties: Dict[str, EntityProperty]


@dataclass
class DataDictRel:
    "Meta relationship entity as specified by the data dict."
    source: str
    target: str
    doc: str
    properties: Dict[str, EntityProperty]


class RawPropertyScalar(TypedDict):
    doc: str
    type: str


class RawPropertyArrayItem(TypedDict):
    type: str


class RawPropertyArray(TypedDict):
    doc: str
    type: Literal["array"]
    items: RawPropertyArrayItem


class RawMetaNode(TypedDict):
    doc: str
    properties: Dict[str, Union[RawPropertyScalar, RawPropertyArray]]
    required: List[str]
    index: str
    meta: Dict[str, str]


class RawMetaRel(TypedDict):
    doc: str
    properties: Dict[str, Union[RawPropertyScalar, RawPropertyArray]]
    required: List[str]
