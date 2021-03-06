import socket
from typing import Any, Optional

from bson.py3compat import integer_types as integer_types
from pymongo import auth as auth
from pymongo import helpers as helpers
from pymongo import thread_util as thread_util
from pymongo.common import MAX_BSON_SIZE as MAX_BSON_SIZE
from pymongo.common import MAX_IDLE_TIME_SEC as MAX_IDLE_TIME_SEC
from pymongo.common import MAX_MESSAGE_SIZE as MAX_MESSAGE_SIZE
from pymongo.common import MAX_POOL_SIZE as MAX_POOL_SIZE
from pymongo.common import MAX_WIRE_VERSION as MAX_WIRE_VERSION
from pymongo.common import MAX_WRITE_BATCH_SIZE as MAX_WRITE_BATCH_SIZE
from pymongo.common import MIN_POOL_SIZE as MIN_POOL_SIZE
from pymongo.common import ORDERED_TYPES as ORDERED_TYPES
from pymongo.common import WAIT_QUEUE_TIMEOUT as WAIT_QUEUE_TIMEOUT
from pymongo.errors import AutoReconnect as AutoReconnect
from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.errors import ConnectionFailure as ConnectionFailure
from pymongo.errors import DocumentTooLarge as DocumentTooLarge
from pymongo.errors import InvalidOperation as InvalidOperation
from pymongo.errors import NetworkTimeout as NetworkTimeout
from pymongo.errors import NotMasterError as NotMasterError
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.errors import PyMongoError as PyMongoError
from pymongo.ismaster import IsMaster as IsMaster
from pymongo.monitoring import ConnectionCheckOutFailedReason as ConnectionCheckOutFailedReason
from pymongo.monitoring import ConnectionClosedReason as ConnectionClosedReason
from pymongo.network import SocketChecker as SocketChecker
from pymongo.network import command as command
from pymongo.network import receive_message as receive_message
from pymongo.read_preferences import ReadPreference as ReadPreference
from pymongo.server_type import SERVER_TYPE as SERVER_TYPE
from pymongo.ssl_match_hostname import CertificateError as CertificateError
from pymongo.ssl_match_hostname import match_hostname as match_hostname

class SSLError(socket.error): ...
class _SSLCertificateError(ValueError): ...

def is_ip_address(address: Any): ...

class PoolOptions:
    def __init__(
        self,
        max_pool_size: Any = ...,
        min_pool_size: Any = ...,
        max_idle_time_seconds: Any = ...,
        connect_timeout: Optional[Any] = ...,
        socket_timeout: Optional[Any] = ...,
        wait_queue_timeout: Any = ...,
        wait_queue_multiple: Optional[Any] = ...,
        ssl_context: Optional[Any] = ...,
        ssl_match_hostname: bool = ...,
        socket_keepalive: bool = ...,
        event_listeners: Optional[Any] = ...,
        appname: Optional[Any] = ...,
        driver: Optional[Any] = ...,
        compression_settings: Optional[Any] = ...,
    ) -> None: ...
    @property
    def non_default_options(self): ...
    @property
    def max_pool_size(self): ...
    @property
    def min_pool_size(self): ...
    @property
    def max_idle_time_seconds(self): ...
    @property
    def connect_timeout(self): ...
    @property
    def socket_timeout(self): ...
    @property
    def wait_queue_timeout(self): ...
    @property
    def wait_queue_multiple(self): ...
    @property
    def ssl_context(self): ...
    @property
    def ssl_match_hostname(self): ...
    @property
    def socket_keepalive(self): ...
    @property
    def event_listeners(self): ...
    @property
    def appname(self): ...
    @property
    def driver(self): ...
    @property
    def compression_settings(self): ...
    @property
    def metadata(self): ...

class SocketInfo:
    sock: Any = ...
    address: Any = ...
    id: Any = ...
    authset: Any = ...
    closed: bool = ...
    last_checkin_time: Any = ...
    performed_handshake: bool = ...
    is_writable: bool = ...
    max_wire_version: Any = ...
    max_bson_size: Any = ...
    max_message_size: Any = ...
    max_write_batch_size: Any = ...
    supports_sessions: bool = ...
    is_mongos: bool = ...
    op_msg_enabled: bool = ...
    listeners: Any = ...
    enabled_for_cmap: Any = ...
    compression_settings: Any = ...
    compression_context: Any = ...
    pool_id: Any = ...
    ready: bool = ...
    def __init__(self, sock: Any, pool: Any, address: Any, id: Any) -> None: ...
    def ismaster(self, metadata: Any, cluster_time: Any): ...
    def command(
        self,
        dbname: Any,
        spec: Any,
        slave_ok: bool = ...,
        read_preference: Any = ...,
        codec_options: Any = ...,
        check: bool = ...,
        allowable_errors: Optional[Any] = ...,
        check_keys: bool = ...,
        read_concern: Optional[Any] = ...,
        write_concern: Optional[Any] = ...,
        parse_write_concern_error: bool = ...,
        collation: Optional[Any] = ...,
        session: Optional[Any] = ...,
        client: Optional[Any] = ...,
        retryable_write: bool = ...,
        publish_events: bool = ...,
        user_fields: Optional[Any] = ...,
    ): ...
    def send_message(self, message: Any, max_doc_size: Any) -> None: ...
    def receive_message(self, request_id: Any): ...
    def legacy_write(self, request_id: Any, msg: Any, max_doc_size: Any, with_last_error: Any): ...
    def write_command(self, request_id: Any, msg: Any): ...
    def check_auth(self, all_credentials: Any) -> None: ...
    def authenticate(self, credentials: Any) -> None: ...
    def validate_session(self, client: Any, session: Any) -> None: ...
    def close_socket(self, reason: Any) -> None: ...
    def send_cluster_time(self, command: Any, session: Any, client: Any) -> None: ...
    def update_last_checkin_time(self) -> None: ...
    def update_is_writable(self, is_writable: Any) -> None: ...
    def idle_time_seconds(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

class _PoolClosedError(PyMongoError): ...

class Pool:
    sockets: Any = ...
    lock: Any = ...
    active_sockets: int = ...
    next_connection_id: int = ...
    closed: bool = ...
    is_writable: Any = ...
    pool_id: int = ...
    pid: Any = ...
    address: Any = ...
    opts: Any = ...
    handshake: Any = ...
    enabled_for_cmap: Any = ...
    socket_checker: Any = ...
    def __init__(self, address: Any, options: Any, handshake: bool = ...) -> None: ...
    def update_is_writable(self, is_writable: Any) -> None: ...
    def reset(self) -> None: ...
    def close(self) -> None: ...
    def remove_stale_sockets(self, reference_pool_id: Any) -> None: ...
    def connect(self): ...
    def get_socket(self, all_credentials: Any, checkout: bool = ...) -> None: ...
    def return_socket(self, sock_info: Any, publish_checkin: bool = ...) -> None: ...
    def __del__(self) -> None: ...
