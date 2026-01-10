from base.db import Database


class KVStore(Database):

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        if key not in self.data:
            return None
        return self.data.get(key)

    def delete(self, key) -> bool:
        return self.data.pop(key, None)

    def exists(self, key) -> bool:
        return key in self.data

    def keys(self):
        return self.data.keys()
