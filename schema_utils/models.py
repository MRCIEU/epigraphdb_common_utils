from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Union

from typing_extensions import Literal, TypedDict

# TODO: document resource fields


class RawResource(TypedDict):
    name: str
    uri: str
    meta_nodes: List[str]
    meta_rels: List[str]
    query_ents: List[str]
    triples: List[str]


class RawWebResourceWithParent(TypedDict):
    name: str
    uri: str
    parent: str


class RawRpkgResourceWithParent(TypedDict):
    uri: str
    parent: str


class RawResources(TypedDict):
    api: Dict[str, RawResource]
    web: Dict[str, Union[RawWebResourceWithParent, RawResource]]
    rpkg: Dict[str, Union[RawRpkgResourceWithParent, RawResource]]


class RawResourcesExtraNode(TypedDict):
    assoc_ent: str
    mapper: str
    queriable: bool


class RawResourcesExtraAssocEnt(TypedDict):
    api: Optional[str]
    web: Optional[str]
    rpkg: Optional[str]


class RawResourcesExtraAssocResourceApi(TypedDict):
    name: str
    uri: str
    label: str


class RawResourcesExtraAssocResourceWeb(TypedDict):
    name: str
    label: str
    url_fn: str


class RawResourcesExtraAssocResources(TypedDict):
    api: Dict[str, RawResourcesExtraAssocResourceApi]
    web: Dict[str, RawResourcesExtraAssocResourceWeb]
    rpkg: Dict[str, RawResourcesExtraAssocResourceApi]


class RawResourcesExtra(TypedDict):
    nodes: Dict[str, List[RawResourcesExtraNode]]
    assoc_ents: Dict[str, RawResourcesExtraAssocEnt]
    assoc_resources: RawResourcesExtraAssocResources


@dataclass
class Resource:
    """A harmonized resource item.

    - Harmonized / standardized from all different
      resource sources (api, rpkg, web)
    - Meta entity level.
    """

    # descriptive label
    label: str
    # uri / id
    uri: str
    # url to resource
    url: str
    # member meta nodes
    meta_nodes: List[str]
    # member meta rels
    meta_rels: List[str]
    # meta ents (meta nodes) as queriable ents
    query_ents: List[str]
    # meta ent triples
    triples: Optional[Set[str]] = None


class EpigraphdbPlatformResources(TypedDict):
    api: Dict[str, Resource]
    web: Dict[str, Resource]
    rpkg: Dict[str, Resource]


@dataclass
class LinkedResource:
    queriable: bool = False


@dataclass
class MetaEntityResources:
    # str here is the key to link to resource
    api: Optional[Dict[str, LinkedResource]]
    web: Optional[Dict[str, LinkedResource]]
    rpkg: Optional[Dict[str, LinkedResource]]


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
