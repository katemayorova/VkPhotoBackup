import json
from json import JSONEncoder


class UploadLog:
    def __init__(self):
        self.log = []

    def append(self, file_name: str, size: int):
        entry = _LogEntry(file_name, size)
        self.log.append(entry)

    def dump_json(self):
        return json.dumps(self.log, cls=_LogEntryEncoder, indent=2)


class _LogEntry:
    def __init__(self, file_name, size):
        self.file_name = file_name
        self.size = size


class _LogEntryEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, _LogEntry):
            return o.__dict__
        else:
            return super().default(o)
