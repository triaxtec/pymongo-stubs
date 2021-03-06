from typing import Any

from pymongo import common as common
from pymongo.server_type import SERVER_TYPE as SERVER_TYPE

class IsMaster:
    def __init__(self, doc: Any) -> None: ...
    @property
    def document(self): ...
    @property
    def server_type(self): ...
    @property
    def all_hosts(self): ...
    @property
    def tags(self): ...
    @property
    def primary(self): ...
    @property
    def replica_set_name(self): ...
    @property
    def max_bson_size(self): ...
    @property
    def max_message_size(self): ...
    @property
    def max_write_batch_size(self): ...
    @property
    def min_wire_version(self): ...
    @property
    def max_wire_version(self): ...
    @property
    def set_version(self): ...
    @property
    def election_id(self): ...
    @property
    def cluster_time(self): ...
    @property
    def logical_session_timeout_minutes(self): ...
    @property
    def is_writable(self): ...
    @property
    def is_readable(self): ...
    @property
    def me(self): ...
    @property
    def last_write_date(self): ...
    @property
    def compressors(self): ...
