from typing import Any, Optional

from bson.errors import *
from pymongo.ssl_match_hostname import CertificateError as CertificateError

class PyMongoError(Exception):
    def __init__(self, message: str = ..., error_labels: Optional[Any] = ...) -> None: ...
    def has_error_label(self, label: Any): ...

class ProtocolError(PyMongoError): ...

class ConnectionFailure(PyMongoError):
    def __init__(self, message: str = ..., error_labels: Optional[Any] = ...) -> None: ...

class AutoReconnect(ConnectionFailure):
    errors: Any = ...
    def __init__(self, message: str = ..., errors: Optional[Any] = ...) -> None: ...

class NetworkTimeout(AutoReconnect): ...
class NotMasterError(AutoReconnect): ...
class ServerSelectionTimeoutError(AutoReconnect): ...
class ConfigurationError(PyMongoError): ...

class OperationFailure(PyMongoError):
    def __init__(self, error: Any, code: Optional[Any] = ..., details: Optional[Any] = ...) -> None: ...
    @property
    def code(self): ...
    @property
    def details(self): ...

class CursorNotFound(OperationFailure): ...
class ExecutionTimeout(OperationFailure): ...
class WriteConcernError(OperationFailure): ...
class WriteError(OperationFailure): ...
class WTimeoutError(WriteConcernError): ...
class DuplicateKeyError(WriteError): ...

class BulkWriteError(OperationFailure):
    def __init__(self, results: Any) -> None: ...

class InvalidOperation(PyMongoError): ...
class InvalidName(PyMongoError): ...
class CollectionInvalid(PyMongoError): ...
class InvalidURI(ConfigurationError): ...
class ExceededMaxWaiters(PyMongoError): ...
class DocumentTooLarge(InvalidDocument): ...

class EncryptionError(PyMongoError):
    def __init__(self, cause: Any) -> None: ...
    @property
    def cause(self): ...