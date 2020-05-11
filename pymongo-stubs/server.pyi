from typing import Any, Optional

from pymongo.errors import NotMasterError as NotMasterError
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.response import ExhaustResponse as ExhaustResponse
from pymongo.response import Response as Response
from pymongo.server_type import SERVER_TYPE as SERVER_TYPE

class Server:
    def __init__(
        self,
        server_description: Any,
        pool: Any,
        monitor: Any,
        topology_id: Optional[Any] = ...,
        listeners: Optional[Any] = ...,
        events: Optional[Any] = ...,
    ) -> None: ...
    def open(self) -> None: ...
    def reset(self) -> None: ...
    def close(self) -> None: ...
    def request_check(self) -> None: ...
    def run_operation_with_response(
        self, sock_info: Any, operation: Any, set_slave_okay: Any, listeners: Any, exhaust: Any, unpack_res: Any
    ): ...
    def get_socket(self, all_credentials: Any, checkout: bool = ...): ...
    @property
    def description(self): ...
    @description.setter
    def description(self, server_description: Any) -> None: ...
    @property
    def pool(self): ...