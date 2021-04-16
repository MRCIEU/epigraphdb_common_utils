from dataclasses import dataclass
from typing import Dict, List, Optional

from typing_extensions import TypedDict


@dataclass
class EntityProperty:
    "The property fields for a meta entity."
    doc: str
    type: str


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


class SchemaExtraEntity(TypedDict):
    api: Optional[List[str]]
    web: Optional[List[str]]
    r: Optional[List[str]]


class SchemaExtra(TypedDict):
    meta_nodes: Dict[str, SchemaExtraEntity]
    meta_rels: Dict[str, SchemaExtraEntity]
