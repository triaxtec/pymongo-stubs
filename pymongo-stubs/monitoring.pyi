from collections import namedtuple
from typing import Any, Optional

_Listeners = namedtuple(
    "Listeners",
    ["command_listeners", "server_listeners", "server_heartbeat_listeners", "topology_listeners", "cmap_listeners"],
)

class _EventListener: ...

class CommandListener(_EventListener):
    def started(self, event: Any) -> None: ...
    def succeeded(self, event: Any) -> None: ...
    def failed(self, event: Any) -> None: ...

class ConnectionPoolListener(_EventListener):
    def pool_created(self, event: Any) -> None: ...
    def pool_cleared(self, event: Any) -> None: ...
    def pool_closed(self, event: Any) -> None: ...
    def connection_created(self, event: Any) -> None: ...
    def connection_ready(self, event: Any) -> None: ...
    def connection_closed(self, event: Any) -> None: ...
    def connection_check_out_started(self, event: Any) -> None: ...
    def connection_check_out_failed(self, event: Any) -> None: ...
    def connection_checked_out(self, event: Any) -> None: ...
    def connection_checked_in(self, event: Any) -> None: ...

class ServerHeartbeatListener(_EventListener):
    def started(self, event: Any) -> None: ...
    def succeeded(self, event: Any) -> None: ...
    def failed(self, event: Any) -> None: ...

class TopologyListener(_EventListener):
    def opened(self, event: Any) -> None: ...
    def description_changed(self, event: Any) -> None: ...
    def closed(self, event: Any) -> None: ...

class ServerListener(_EventListener):
    def opened(self, event: Any) -> None: ...
    def description_changed(self, event: Any) -> None: ...
    def closed(self, event: Any) -> None: ...

def register(listener: Any) -> None: ...

class _CommandEvent:
    def __init__(self, command_name: Any, request_id: Any, connection_id: Any, operation_id: Any) -> None: ...
    @property
    def command_name(self): ...
    @property
    def request_id(self): ...
    @property
    def connection_id(self): ...
    @property
    def operation_id(self): ...

class CommandStartedEvent(_CommandEvent):
    def __init__(self, command: Any, database_name: Any, *args: Any) -> None: ...
    @property
    def command(self): ...
    @property
    def database_name(self): ...

class CommandSucceededEvent(_CommandEvent):
    def __init__(
        self, duration: Any, reply: Any, command_name: Any, request_id: Any, connection_id: Any, operation_id: Any
    ) -> None: ...
    @property
    def duration_micros(self): ...
    @property
    def reply(self): ...

class CommandFailedEvent(_CommandEvent):
    def __init__(self, duration: Any, failure: Any, *args: Any) -> None: ...
    @property
    def duration_micros(self): ...
    @property
    def failure(self): ...

class _PoolEvent:
    def __init__(self, address: Any) -> None: ...
    @property
    def address(self): ...

class PoolCreatedEvent(_PoolEvent):
    def __init__(self, address: Any, options: Any) -> None: ...
    @property
    def options(self): ...

class PoolClearedEvent(_PoolEvent): ...
class PoolClosedEvent(_PoolEvent): ...

class ConnectionClosedReason:
    STALE: str = ...
    IDLE: str = ...
    ERROR: str = ...
    POOL_CLOSED: str = ...

class ConnectionCheckOutFailedReason:
    TIMEOUT: str = ...
    POOL_CLOSED: str = ...
    CONN_ERROR: str = ...

class _ConnectionEvent:
    def __init__(self, address: Any, connection_id: Any) -> None: ...
    @property
    def address(self): ...
    @property
    def connection_id(self): ...

class ConnectionCreatedEvent(_ConnectionEvent): ...
class ConnectionReadyEvent(_ConnectionEvent): ...

class ConnectionClosedEvent(_ConnectionEvent):
    def __init__(self, address: Any, connection_id: Any, reason: Any) -> None: ...
    @property
    def reason(self): ...

class ConnectionCheckOutStartedEvent:
    def __init__(self, address: Any) -> None: ...
    @property
    def address(self): ...

class ConnectionCheckOutFailedEvent:
    def __init__(self, address: Any, reason: Any) -> None: ...
    @property
    def address(self): ...
    @property
    def reason(self): ...

class ConnectionCheckedOutEvent(_ConnectionEvent): ...
class ConnectionCheckedInEvent(_ConnectionEvent): ...

class _ServerEvent:
    def __init__(self, server_address: Any, topology_id: Any) -> None: ...
    @property
    def server_address(self): ...
    @property
    def topology_id(self): ...

class ServerDescriptionChangedEvent(_ServerEvent):
    def __init__(self, previous_description: Any, new_description: Any, *args: Any) -> None: ...
    @property
    def previous_description(self): ...
    @property
    def new_description(self): ...

class ServerOpeningEvent(_ServerEvent): ...
class ServerClosedEvent(_ServerEvent): ...

class TopologyEvent:
    def __init__(self, topology_id: Any) -> None: ...
    @property
    def topology_id(self): ...

class TopologyDescriptionChangedEvent(TopologyEvent):
    def __init__(self, previous_description: Any, new_description: Any, *args: Any) -> None: ...
    @property
    def previous_description(self): ...
    @property
    def new_description(self): ...

class TopologyOpenedEvent(TopologyEvent): ...
class TopologyClosedEvent(TopologyEvent): ...

class _ServerHeartbeatEvent:
    def __init__(self, connection_id: Any) -> None: ...
    @property
    def connection_id(self): ...

class ServerHeartbeatStartedEvent(_ServerHeartbeatEvent): ...

class ServerHeartbeatSucceededEvent(_ServerHeartbeatEvent):
    def __init__(self, duration: Any, reply: Any, *args: Any) -> None: ...
    @property
    def duration(self): ...
    @property
    def reply(self): ...

class ServerHeartbeatFailedEvent(_ServerHeartbeatEvent):
    def __init__(self, duration: Any, reply: Any, *args: Any) -> None: ...
    @property
    def duration(self): ...
    @property
    def reply(self): ...

class _EventListeners:
    def __init__(self, listeners: Any) -> None: ...
    @property
    def enabled_for_commands(self): ...
    @property
    def enabled_for_server(self): ...
    @property
    def enabled_for_server_heartbeat(self): ...
    @property
    def enabled_for_topology(self): ...
    @property
    def enabled_for_cmap(self): ...
    def event_listeners(self): ...
    def publish_command_start(
        self, command: Any, database_name: Any, request_id: Any, connection_id: Any, op_id: Optional[Any] = ...
    ) -> None: ...
    def publish_command_success(
        self,
        duration: Any,
        reply: Any,
        command_name: Any,
        request_id: Any,
        connection_id: Any,
        op_id: Optional[Any] = ...,
    ) -> None: ...
    def publish_command_failure(
        self,
        duration: Any,
        failure: Any,
        command_name: Any,
        request_id: Any,
        connection_id: Any,
        op_id: Optional[Any] = ...,
    ) -> None: ...
    def publish_server_heartbeat_started(self, connection_id: Any) -> None: ...
    def publish_server_heartbeat_succeeded(self, connection_id: Any, duration: Any, reply: Any) -> None: ...
    def publish_server_heartbeat_failed(self, connection_id: Any, duration: Any, reply: Any) -> None: ...
    def publish_server_opened(self, server_address: Any, topology_id: Any) -> None: ...
    def publish_server_closed(self, server_address: Any, topology_id: Any) -> None: ...
    def publish_server_description_changed(
        self, previous_description: Any, new_description: Any, server_address: Any, topology_id: Any
    ) -> None: ...
    def publish_topology_opened(self, topology_id: Any) -> None: ...
    def publish_topology_closed(self, topology_id: Any) -> None: ...
    def publish_topology_description_changed(
        self, previous_description: Any, new_description: Any, topology_id: Any
    ) -> None: ...
    def publish_pool_created(self, address: Any, options: Any) -> None: ...
    def publish_pool_cleared(self, address: Any) -> None: ...
    def publish_pool_closed(self, address: Any) -> None: ...
    def publish_connection_created(self, address: Any, connection_id: Any) -> None: ...
    def publish_connection_ready(self, address: Any, connection_id: Any) -> None: ...
    def publish_connection_closed(self, address: Any, connection_id: Any, reason: Any) -> None: ...
    def publish_connection_check_out_started(self, address: Any) -> None: ...
    def publish_connection_check_out_failed(self, address: Any, reason: Any) -> None: ...
    def publish_connection_checked_out(self, address: Any, connection_id: Any) -> None: ...
    def publish_connection_checked_in(self, address: Any, connection_id: Any) -> None: ...
