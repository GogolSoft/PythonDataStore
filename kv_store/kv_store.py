# Create, Open, Read, Save (key/value)
# kv_store = KVStore() - memory
# kv_store = KVStore('path-to-your-db)
# kv set (key, value)
# kv get, delete, exists, count, keys, save, save(path)
import json

from base.db import Database


class KVStore(Database):

    def set(self, key, value):
        self.data[key] = value

    def save(self):
        if self.path is None:
            return
        with open(self.path, 'w+') as new_version:
            json.dump(self.data, new_version, indent=4)

    def get(self, key):
        return self.data[key]

    def delete(self, key) -> bool:
        try:
            self.data.pop(key)
            return True
        except KeyError:
            return False

    def exists(self, key) -> bool:
        return key in self.data

    def keys(self):
        return self.data.keys()


