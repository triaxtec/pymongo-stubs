from typing import Any

from pymongo import mongo_client as mongo_client

class MongoReplicaSetClient(mongo_client.MongoClient):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
