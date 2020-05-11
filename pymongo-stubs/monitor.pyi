from typing import Any, Optional

from pymongo import common as common
from pymongo import periodic_executor as periodic_executor
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.read_preferences import MovingAverage as MovingAverage
from pymongo.server_description import ServerDescription as ServerDescription
from pymongo.server_type import SERVER_TYPE as SERVER_TYPE

class MonitorBase:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def join(self, timeout: Optional[Any] = ...) -> None: ...
    def request_check(self) -> None: ...

class Monitor(MonitorBase):
    def __init__(self, server_description: Any, topology: Any, pool: Any, topology_settings: Any): ...
    def close(self) -> None: ...

class SrvMonitor(MonitorBase):
    def __init__(self, topology: Any, topology_settings: Any): ...
