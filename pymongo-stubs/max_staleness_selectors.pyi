from typing import Any

from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.server_type import SERVER_TYPE as SERVER_TYPE

IDLE_WRITE_PERIOD: int
SMALLEST_MAX_STALENESS: int

def select(max_staleness: Any, selection: Any): ...
