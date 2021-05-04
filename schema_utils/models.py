from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Union

from typing_extensions import Literal, TypedDict


@dataclass
class EntityProperty:
    "The property fields for a meta entity."
    doc: str
    type: str
    required: bool


@dataclass
class Resource:
    label: str
    uri: str
    url: str
    meta_nodes: List[str]
    meta_rels: List[str]
    query_ents: List[str]
    triples: Optional[Set[str]] = None
    # TODO: this should probably go
    assoc_ents: Optional[List[str]] = None


@dataclass
class LinkedResource:
    queriable: bool = False


@dataclass
class MetaEntityResources:
    api: Optional[Dict[str, LinkedResource]]
    web: Optional[Dict[str, LinkedResource]]
    rpkg: Optional[Dict[str, LinkedResource]]


@dataclass
class DataDictNode:
    "Meta node entity as specified by the data dict."
    id: str
    name: str
    doc: str
    properties: Dict[str, EntityProperty]
    resources: MetaEntityResources


@dataclass
class DataDictRel:
    "Meta relationship entity as specified by the data dict."
    source: str
    target: str
    doc: str
    properties: Dict[str, EntityProperty]
    resources: MetaEntityResources


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
