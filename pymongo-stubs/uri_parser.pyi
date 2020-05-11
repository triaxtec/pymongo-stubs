from typing import Any, Optional

from pymongo.common import INTERNAL_URI_OPTION_NAME_MAP as INTERNAL_URI_OPTION_NAME_MAP
from pymongo.common import URI_OPTIONS_DEPRECATION_MAP as URI_OPTIONS_DEPRECATION_MAP
from pymongo.common import get_validated_options as get_validated_options
from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.errors import InvalidURI as InvalidURI

SCHEME: str
SCHEME_LEN: Any
SRV_SCHEME: str
SRV_SCHEME_LEN: Any
DEFAULT_PORT: int

def parse_userinfo(userinfo: Any): ...
def parse_ipv6_literal_host(entity: Any, default_port: Any): ...
def parse_host(entity: Any, default_port: Any = ...): ...
def validate_options(opts: Any, warn: bool = ...): ...
def split_options(opts: Any, validate: bool = ..., warn: bool = ..., normalize: bool = ...): ...
def split_hosts(hosts: Any, default_port: Any = ...): ...
def parse_uri(
    uri: Any,
    default_port: Any = ...,
    validate: bool = ...,
    warn: bool = ...,
    normalize: bool = ...,
    connect_timeout: Optional[Any] = ...,
): ...
