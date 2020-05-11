from typing import Any, Optional

from pymongo import common as common
from pymongo import monitor as monitor
from pymongo import pool as pool
from pymongo.common import LOCAL_THRESHOLD_MS as LOCAL_THRESHOLD_MS
from pymongo.common import SERVER_SELECTION_TIMEOUT as SERVER_SELECTION_TIMEOUT
from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.pool import PoolOptions as PoolOptions
from pymongo.server_description import ServerDescription as ServerDescription
from pymongo.topology_description import TOPOLOGY_TYPE as TOPOLOGY_TYPE

class TopologySettings:
    def __init__(
        self,
        seeds: Optional[Any] = ...,
        replica_set_name: Optional[Any] = ...,
        pool_class: Optional[Any] = ...,
        pool_options: Optional[Any] = ...,
        monitor_class: Optional[Any] = ...,
        condition_class: Optional[Any] = ...,
        local_threshold_ms: Any = ...,
        server_selection_timeout: Any = ...,
        heartbeat_frequency: Any = ...,
        server_selector: Optional[Any] = ...,
        fqdn: Optional[Any] = ...,
    ) -> None: ...
    @property
    def seeds(self): ...
    @property
    def replica_set_name(self): ...
    @property
    def pool_class(self): ...
    @property
    def pool_options(self): ...
    @property
    def monitor_class(self): ...
    @property
    def condition_class(self): ...
    @property
    def local_threshold_ms(self): ...
    @property
    def server_selection_timeout(self): ...
    @property
    def server_selector(self): ...
    @property
    def heartbeat_frequency(self): ...
    @property
    def fqdn(self): ...
    @property
    def direct(self): ...
    def get_topology_type(self): ...
    def get_server_descriptions(self): ...
