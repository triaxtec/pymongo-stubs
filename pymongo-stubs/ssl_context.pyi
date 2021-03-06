from typing import Any, Optional

class SSLContext:
    def __init__(self, protocol: Any) -> None: ...
    @property
    def protocol(self): ...
    verify_mode: Any = ...
    def load_cert_chain(self, certfile: Any, keyfile: Optional[Any] = ...) -> None: ...
    def load_verify_locations(self, cafile: Optional[Any] = ..., dummy: Optional[Any] = ...) -> None: ...
    def wrap_socket(
        self,
        sock: Any,
        server_side: bool = ...,
        do_handshake_on_connect: bool = ...,
        suppress_ragged_eofs: bool = ...,
        dummy: Optional[Any] = ...,
    ): ...
