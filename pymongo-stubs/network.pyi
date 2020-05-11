from typing import Any, Optional

from pymongo import helpers as helpers
from pymongo import message as message
from pymongo.common import MAX_MESSAGE_SIZE as MAX_MESSAGE_SIZE
from pymongo.compression_support import decompress as decompress
from pymongo.errors import AutoReconnect as AutoReconnect
from pymongo.errors import NotMasterError as NotMasterError
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.errors import ProtocolError as ProtocolError

def command(
    sock: Any,
    dbname: Any,
    spec: Any,
    slave_ok: Any,
    is_mongos: Any,
    read_preference: Any,
    codec_options: Any,
    session: Any,
    client: Any,
    check: bool = ...,
    allowable_errors: Optional[Any] = ...,
    address: Optional[Any] = ...,
    check_keys: bool = ...,
    listeners: Optional[Any] = ...,
    max_bson_size: Optional[Any] = ...,
    read_concern: Optional[Any] = ...,
    parse_write_concern_error: bool = ...,
    collation: Optional[Any] = ...,
    compression_ctx: Optional[Any] = ...,
    use_op_msg: bool = ...,
    unacknowledged: bool = ...,
    user_fields: Optional[Any] = ...,
): ...
def receive_message(sock: Any, request_id: Any, max_message_size: Any = ...): ...

class SocketChecker:
    def __init__(self) -> None: ...
    def socket_closed(self, sock: Any): ...
