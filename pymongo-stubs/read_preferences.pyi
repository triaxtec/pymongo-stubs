from typing import Any, Optional

from pymongo import max_staleness_selectors as max_staleness_selectors
from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.server_selectors import member_with_tags_server_selector as member_with_tags_server_selector
from pymongo.server_selectors import secondary_with_tags_server_selector as secondary_with_tags_server_selector

class _ServerMode:
    def __init__(self, mode: Any, tag_sets: Optional[Any] = ..., max_staleness: int = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def mongos_mode(self): ...
    @property
    def document(self): ...
    @property
    def mode(self): ...
    @property
    def tag_sets(self): ...
    @property
    def max_staleness(self): ...
    @property
    def min_wire_version(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

class Primary(_ServerMode):
    def __init__(self) -> None: ...
    def __call__(self, selection: Any): ...
    def __eq__(self, other: Any) -> Any: ...

class PrimaryPreferred(_ServerMode):
    def __init__(self, tag_sets: Optional[Any] = ..., max_staleness: int = ...) -> None: ...
    def __call__(self, selection: Any): ...

class Secondary(_ServerMode):
    def __init__(self, tag_sets: Optional[Any] = ..., max_staleness: int = ...) -> None: ...
    def __call__(self, selection: Any): ...

class SecondaryPreferred(_ServerMode):
    def __init__(self, tag_sets: Optional[Any] = ..., max_staleness: int = ...) -> None: ...
    def __call__(self, selection: Any): ...

class Nearest(_ServerMode):
    def __init__(self, tag_sets: Optional[Any] = ..., max_staleness: int = ...) -> None: ...
    def __call__(self, selection: Any): ...

def make_read_preference(mode: Any, tag_sets: Any, max_staleness: int = ...): ...

class ReadPreference:
    PRIMARY: Any = ...
    PRIMARY_PREFERRED: Any = ...
    SECONDARY: Any = ...
    SECONDARY_PREFERRED: Any = ...
    NEAREST: Any = ...

def read_pref_mode_from_name(name: Any): ...

class MovingAverage:
    average: Any = ...
    def __init__(self) -> None: ...
    def add_sample(self, sample: Any) -> None: ...
    def get(self): ...
    def reset(self) -> None: ...
