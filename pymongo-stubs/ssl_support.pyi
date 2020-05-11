from typing import Any

from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.ssl_context import SSLContext as SSLContext

HAVE_SSL: bool
HAVE_CERTIFI: bool
HAVE_WINCERTSTORE: bool

def validate_cert_reqs(option: Any, value: Any): ...
def validate_allow_invalid_certs(option: Any, value: Any): ...
def get_ssl_context(*args: Any): ...
