import json

from base.db import Database


class TableStore(Database):

    def set(self, key, value):
        if not isinstance(value, dict):
            raise TypeError("TableStore can only store dictionaries like {columnName : columnValue}")
        self.data[key] = value

    def save(self):
        if self.path is None:
            return
        with open(self.path, 'w+') as new_version:
            json.dump(self.data, new_version, indent=4)

    def get(self, key):
        return self.data.get(key)

    def get_all_by_attribute(self, attribute_name, value):
        matches = []
        for row in self.data.items():
            values_dict = row[1]
            attr = values_dict.get(attribute_name)
            if attr == value:
                matches.append(row)
        return matches

    def get_by_id(self, key):
        return self.data.get(key)

    def delete(self, key):
        return self.data.pop(key)
