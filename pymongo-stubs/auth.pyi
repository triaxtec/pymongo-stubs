from collections import namedtuple
from typing import Any

from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.saslprep import saslprep as saslprep

HAVE_KERBEROS: bool
MECHANISMS: Any

class _Cache:
    data: Any = ...
    def __init__(self) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

MongoCredential = namedtuple(
    "MongoCredential", ["mechanism", "source", "username", "password", "mechanism_properties", "cache"]
)

GSSAPIProperties = namedtuple("GSSAPIProperties", ["service_name", "canonicalize_host_name", "service_realm"])

def authenticate(credentials: Any, sock_info: Any) -> None: ...
def logout(source: Any, sock_info: Any) -> None: ...
