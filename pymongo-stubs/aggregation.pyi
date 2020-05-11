from typing import Any, Optional

from pymongo import common as common
from pymongo.collation import validate_collation_or_none as validate_collation_or_none
from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.read_preferences import ReadPreference as ReadPreference

class _AggregationCommand:
    def __init__(
        self,
        target: Any,
        cursor_class: Any,
        pipeline: Any,
        options: Any,
        explicit_session: Any,
        user_fields: Optional[Any] = ...,
        result_processor: Optional[Any] = ...,
    ) -> None: ...
    def get_read_preference(self, session: Any): ...
    def get_cursor(self, session: Any, server: Any, sock_info: Any, slave_ok: Any): ...

class _CollectionAggregationCommand(_AggregationCommand):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class _CollectionRawAggregationCommand(_CollectionAggregationCommand):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class _DatabaseAggregationCommand(_AggregationCommand): ...
