from typing import Any

class Response:
    def __init__(
        self, data: Any, address: Any, request_id: Any, duration: Any, from_command: Any, docs: Any
    ) -> None: ...
    @property
    def data(self): ...
    @property
    def address(self): ...
    @property
    def request_id(self): ...
    @property
    def duration(self): ...
    @property
    def from_command(self): ...
    @property
    def docs(self): ...

class ExhaustResponse(Response):
    def __init__(
        self,
        data: Any,
        address: Any,
        socket_info: Any,
        pool: Any,
        request_id: Any,
        duration: Any,
        from_command: Any,
        docs: Any,
    ) -> None: ...
    @property
    def socket_info(self): ...
    @property
    def pool(self): ...
