from typing import Dict

from pydantic.dataclasses import dataclass


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
