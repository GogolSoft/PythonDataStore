import json
from pathlib import Path


class Database:
    def __init__(self, name, location=None):
        self.name = name
        self.data = {}
        self.path = Path(location) if location else None

        if self.path is None:
            return

        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.touch()
            self.path.write_text(json.dumps(self.data), encoding="utf-8")

        elif self.path.is_file():
            with open(self.path, 'r+') as existing_file:
                self.data = json.load(existing_file)

    def save(self):
        if self.path is None:
            return
        with open(self.path, 'w+') as new_version:
            json.dump(self.data, new_version, indent=4)
