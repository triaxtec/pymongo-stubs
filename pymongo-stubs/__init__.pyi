from typing import Tuple

from pymongo.collection import ReturnDocument as ReturnDocument
from pymongo.common import MAX_SUPPORTED_WIRE_VERSION as MAX_SUPPORTED_WIRE_VERSION
from pymongo.common import MIN_SUPPORTED_WIRE_VERSION as MIN_SUPPORTED_WIRE_VERSION
from pymongo.cursor import CursorType as CursorType
from pymongo.mongo_client import MongoClient as MongoClient
from pymongo.mongo_replica_set_client import MongoReplicaSetClient as MongoReplicaSetClient
from pymongo.operations import DeleteMany as DeleteMany
from pymongo.operations import DeleteOne as DeleteOne
from pymongo.operations import IndexModel as IndexModel
from pymongo.operations import InsertOne as InsertOne
from pymongo.operations import ReplaceOne as ReplaceOne
from pymongo.operations import UpdateMany as UpdateMany
from pymongo.operations import UpdateOne as UpdateOne
from pymongo.read_preferences import ReadPreference as ReadPreference
from pymongo.write_concern import WriteConcern as WriteConcern

ASCENDING: int
DESCENDING: int
GEO2D: str
GEOHAYSTACK: str
GEOSPHERE: str
HASHED: str
TEXT: str
OFF: int
SLOW_ONLY: int
ALL: int
version_tuple: Tuple[int, int, int]

def get_version_string() -> str: ...

version: str

def has_c() -> bool: ...
