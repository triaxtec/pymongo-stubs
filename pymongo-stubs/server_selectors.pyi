from typing import Any

from pymongo.server_type import SERVER_TYPE as SERVER_TYPE

class Selection:
    @classmethod
    def from_topology_description(cls, topology_description: Any): ...
    topology_description: Any = ...
    server_descriptions: Any = ...
    primary: Any = ...
    common_wire_version: Any = ...
    def __init__(
        self, topology_description: Any, server_descriptions: Any, common_wire_version: Any, primary: Any
    ) -> None: ...
    def with_server_descriptions(self, server_descriptions: Any): ...
    def secondary_with_max_last_write_date(self): ...
    @property
    def primary_selection(self): ...
    @property
    def heartbeat_frequency(self): ...
    @property
    def topology_type(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def __getitem__(self, item: Any): ...

def any_server_selector(selection: Any): ...
def readable_server_selector(selection: Any): ...
def writable_server_selector(selection: Any): ...
def secondary_server_selector(selection: Any): ...
def arbiter_server_selector(selection: Any): ...
def writable_preferred_server_selector(selection: Any): ...
def apply_single_tag_set(tag_set: Any, selection: Any): ...
def apply_tag_sets(tag_sets: Any, selection: Any): ...
def secondary_with_tags_server_selector(tag_sets: Any, selection: Any): ...
def member_with_tags_server_selector(tag_sets: Any, selection: Any): ...
