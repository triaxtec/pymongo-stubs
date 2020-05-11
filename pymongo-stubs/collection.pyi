from typing import Any, List, Optional, Tuple, Union

from pymongo import common as common
from pymongo import helpers as helpers
from pymongo import message as message
from pymongo.bulk import BulkOperationBuilder as BulkOperationBuilder
from pymongo.change_stream import CollectionChangeStream as CollectionChangeStream
from pymongo.client_session import ClientSession
from pymongo.collation import validate_collation_or_none as validate_collation_or_none, Collation
from pymongo.command_cursor import CommandCursor as CommandCursor
from pymongo.command_cursor import RawBatchCommandCursor as RawBatchCommandCursor
from pymongo.common import ORDERED_TYPES as ORDERED_TYPES
from pymongo.cursor import Cursor as Cursor
from pymongo.cursor import RawBatchCursor as RawBatchCursor
from pymongo.database import Database
from pymongo.errors import BulkWriteError as BulkWriteError
from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.errors import InvalidName as InvalidName
from pymongo.errors import InvalidOperation as InvalidOperation
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.operations import IndexModel as IndexModel
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import ReadPreference as ReadPreference
from pymongo.results import BulkWriteResult as BulkWriteResult
from pymongo.results import DeleteResult as DeleteResult
from pymongo.results import InsertManyResult as InsertManyResult
from pymongo.results import InsertOneResult as InsertOneResult
from pymongo.results import UpdateResult as UpdateResult
from pymongo.write_concern import WriteConcern as WriteConcern

class ReturnDocument:
    BEFORE: bool = ...
    AFTER: bool = ...

class Collection(common.BaseObject):
    def __init__(
        self,
        database: Any,
        name: Any,
        create: bool = ...,
        codec_options: Optional[Any] = ...,
        read_preference: Optional[ReadPreference] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> None: ...
    def __getattr__(self, name: Any) -> Collection: ...
    def __getitem__(self, name: Any) -> Collection: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    @property
    def full_name(self): ...
    @property
    def name(self): ...
    @property
    def database(self) -> Database: ...
    def with_options(
        self,
        codec_options: Optional[Any] = ...,
        read_preference: Optional[ReadPreference] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
    ): ...
    def initialize_unordered_bulk_op(self, bypass_document_validation: bool = ...): ...
    def initialize_ordered_bulk_op(self, bypass_document_validation: bool = ...): ...
    def bulk_write(
        self, requests: Any, ordered: bool = ..., bypass_document_validation: bool = ..., session: Optional[Any] = ...
    ): ...
    def insert_one(self, document: Any, bypass_document_validation: bool = ..., session: Optional[ClientSession] = ...): ...
    def insert_many(
        self, documents: Any, ordered: bool = ..., bypass_document_validation: bool = ..., session: Optional[ClientSession] = ...
    ): ...
    def replace_one(
        self,
        filter: Any,
        replacement: Any,
        upsert: bool = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Collation] = ...,
        session: Optional[ClientSession] = ...,
    ): ...
    def update_one(
        self,
        filter: Any,
        update: Any,
        upsert: bool = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Collation] = ...,
        array_filters: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ): ...
    def update_many(
        self,
        filter: Any,
        update: Any,
        upsert: bool = ...,
        array_filters: Optional[Any] = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Collation] = ...,
        session: Optional[ClientSession] = ...,
    ): ...
    def drop(self, session: Optional[Any] = ...) -> None: ...
    def delete_one(self, filter: Any, collation: Optional[Collation] = ..., session: Optional[ClientSession] = ...) -> DeleteResult: ...
    def delete_many(self, filter: Any, collation: Optional[Collation] = ..., session: Optional[ClientSession] = ...) -> DeleteResult: ...
    def find_one(self, filter: Optional[Any] = ..., *args: Any, **kwargs: Any): ...
    def find(self, *args: Any, **kwargs: Any): ...
    def find_raw_batches(self, *args: Any, **kwargs: Any): ...
    def parallel_scan(self, num_cursors: Any, session: Optional[Any] = ..., **kwargs: Any): ...
    def estimated_document_count(self, **kwargs: Any): ...
    def count_documents(self, filter: Any, session: Optional[Any] = ..., **kwargs: Any): ...
    def count(self, filter: Optional[Any] = ..., session: Optional[Any] = ..., **kwargs: Any): ...
    def create_indexes(self, indexes: Any, session: Optional[Any] = ..., **kwargs: Any): ...
    def create_index(
        self,
        keys: Union[str, List[Tuple[str, Union[int, str]]]],  # This should be literals of constants in inits
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ): ...
    def ensure_index(self, key_or_list: Any, cache_for: int = ..., **kwargs: Any): ...
    def drop_indexes(self, session: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def drop_index(self, index_or_name: Any, session: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def reindex(self, session: Optional[Any] = ..., **kwargs: Any): ...
    def list_indexes(self, session: Optional[Any] = ...): ...
    def index_information(self, session: Optional[Any] = ...): ...
    def options(self, session: Optional[Any] = ...): ...
    def aggregate(self, pipeline: Any, session: Optional[ClientSession] = ..., **kwargs: Any) -> CommandCursor: ...
    def aggregate_raw_batches(self, pipeline: Any, **kwargs: Any): ...
    def watch(
        self,
        pipeline: Optional[Any] = ...,
        full_document: Optional[Any] = ...,
        resume_after: Optional[Any] = ...,
        max_await_time_ms: Optional[Any] = ...,
        batch_size: Optional[Any] = ...,
        collation: Optional[Collation] = ...,
        start_at_operation_time: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
        start_after: Optional[Any] = ...,
    ): ...
    def group(
        self, key: Any, condition: Any, initial: Any, reduce: Any, finalize: Optional[Any] = ..., **kwargs: Any
    ): ...
    def rename(self, new_name: Any, session: Optional[Any] = ..., **kwargs: Any): ...
    def distinct(self, key: Any, filter: Optional[Any] = ..., session: Optional[Any] = ..., **kwargs: Any): ...
    def map_reduce(
        self, map: Any, reduce: Any, out: Any, full_response: bool = ..., session: Optional[Any] = ..., **kwargs: Any
    ): ...
    def inline_map_reduce(
        self, map: Any, reduce: Any, full_response: bool = ..., session: Optional[Any] = ..., **kwargs: Any
    ): ...
    def find_one_and_delete(
        self,
        filter: Any,
        projection: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        session: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def find_one_and_replace(
        self,
        filter: Any,
        replacement: Any,
        projection: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        upsert: bool = ...,
        return_document: Any = ...,
        session: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def find_one_and_update(
        self,
        filter: Any,
        update: Any,
        projection: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        upsert: bool = ...,
        return_document: Any = ...,
        array_filters: Optional[Any] = ...,
        session: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def save(self, to_save: Any, manipulate: bool = ..., check_keys: bool = ..., **kwargs: Any): ...
    def insert(
        self,
        doc_or_docs: Any,
        manipulate: bool = ...,
        check_keys: bool = ...,
        continue_on_error: bool = ...,
        **kwargs: Any,
    ): ...
    def update(
        self,
        spec: Any,
        document: Any,
        upsert: bool = ...,
        manipulate: bool = ...,
        multi: bool = ...,
        check_keys: bool = ...,
        **kwargs: Any,
    ): ...
    def remove(self, spec_or_id: Optional[Any] = ..., multi: bool = ..., **kwargs: Any): ...
    def find_and_modify(
        self,
        query: Any = ...,
        update: Optional[Any] = ...,
        upsert: bool = ...,
        sort: Optional[Any] = ...,
        full_response: bool = ...,
        manipulate: bool = ...,
        **kwargs: Any,
    ): ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> None: ...
    next: Any = ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
