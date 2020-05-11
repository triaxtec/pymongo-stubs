from typing import Any, Optional, Collection, Dict

from pymongo.collation import validate_collation_or_none as validate_collation_or_none, Collation
from pymongo.common import validate_is_document_type as validate_is_document_type
from pymongo.common import validate_is_mapping as validate_is_mapping
from pymongo.common import validate_ok_for_replace as validate_ok_for_replace
from pymongo.common import validate_ok_for_update as validate_ok_for_update
from pymongo.errors import BulkWriteError as BulkWriteError
from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.errors import InvalidOperation as InvalidOperation
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.read_preferences import ReadPreference as ReadPreference
from pymongo.write_concern import WriteConcern as WriteConcern

class _Run:
    op_type: Any = ...
    index_map: Any = ...
    ops: Any = ...
    idx_offset: int = ...
    def __init__(self, op_type: Any) -> None: ...
    def index(self, idx: Any): ...
    def add(self, original_index: Any, operation: Any) -> None: ...

class _Bulk:
    collection: Any = ...
    ordered: Any = ...
    ops: Any = ...
    executed: bool = ...
    bypass_doc_val: Any = ...
    uses_collation: bool = ...
    uses_array_filters: bool = ...
    is_retryable: bool = ...
    retrying: bool = ...
    started_retryable_write: bool = ...
    current_run: Any = ...
    def __init__(self, collection: Any, ordered: Any, bypass_document_validation: Any) -> None: ...
    @property
    def bulk_ctx_class(self): ...
    def add_insert(self, document: Any) -> None: ...
    def add_update(
        self,
        selector: Any,
        update: Any,
        multi: bool = ...,
        upsert: bool = ...,
        collation: Optional[Any] = ...,
        array_filters: Optional[Any] = ...,
    ) -> None: ...
    def add_replace(
        self, selector: Any, replacement: Any, upsert: bool = ..., collation: Optional[Any] = ...
    ) -> None: ...
    def add_delete(self, selector: Any, limit: Any, collation: Optional[Any] = ...) -> None: ...
    def gen_ordered(self) -> None: ...
    def gen_unordered(self) -> None: ...
    def execute_command(self, generator: Any, write_concern: Any, session: Any): ...
    def execute_insert_no_results(self, sock_info: Any, run: Any, op_id: Any, acknowledged: Any) -> None: ...
    def execute_op_msg_no_results(self, sock_info: Any, generator: Any) -> None: ...
    def execute_command_no_results(self, sock_info: Any, generator: Any) -> None: ...
    def execute_no_results(self, sock_info: Any, generator: Any): ...
    def execute(self, write_concern: Any, session: Any): ...

class BulkUpsertOperation:
    def __init__(self, selector: Any, bulk: Any, collation: Any) -> None: ...
    def update_one(self, update: Dict) -> None: ...
    def update(self, update: Dict) -> None: ...
    def replace_one(self, replacement: Dict) -> None: ...

class BulkWriteOperation:
    def __init__(self, selector: Any, bulk: Any, collation: Any) -> None: ...
    def update_one(self, update: Dict) -> None: ...
    def update(self, update: Dict) -> None: ...
    def replace_one(self, replacement: Dict) -> None: ...
    def remove_one(self) -> None: ...
    def remove(self) -> None: ...
    def upsert(self): ...

class BulkOperationBuilder:
    def __init__(self, collection: Collection, ordered: bool = ..., bypass_document_validation: bool = ...) -> None: ...
    def find(self, selector: Dict, collation: Optional[Collation] = ...): ...
    def insert(self, document: Dict) -> None: ...
    def execute(self, write_concern: Optional[WriteConcern] = ...): ...
