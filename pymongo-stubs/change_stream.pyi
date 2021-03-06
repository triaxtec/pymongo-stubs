from typing import Any

from pymongo import common as common
from pymongo.collation import validate_collation_or_none as validate_collation_or_none
from pymongo.command_cursor import CommandCursor as CommandCursor
from pymongo.errors import ConnectionFailure as ConnectionFailure
from pymongo.errors import InvalidOperation as InvalidOperation
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.errors import PyMongoError as PyMongoError

class ChangeStream:
    def __init__(
        self,
        target: Any,
        pipeline: Any,
        full_document: Any,
        resume_after: Any,
        max_await_time_ms: Any,
        batch_size: Any,
        collation: Any,
        start_at_operation_time: Any,
        session: Any,
        start_after: Any,
    ) -> None: ...
    def close(self) -> None: ...
    def __iter__(self) -> Any: ...
    @property
    def resume_token(self): ...
    def next(self): ...
    __next__: Any = ...
    @property
    def alive(self) -> bool: ...
    def try_next(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

class CollectionChangeStream(ChangeStream): ...
class DatabaseChangeStream(ChangeStream): ...
class ClusterChangeStream(DatabaseChangeStream): ...
