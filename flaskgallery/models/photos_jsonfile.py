import json


class PhotoCollectionJSONFile:
    _dblocation = ''

    def __init__(self, dblocation):
        self._dblocation = dblocation

    def fetchall(self):
        with open(self._dblocation, 'r') as file:
            data = json.load(file)
        return data

    def fetchone(self, objectID):
        for record in self.fetchall():
            if str(record['objectID']) == str(objectID):
                return record
        return None

    def addone(self, photo):
        raise NotImplementedError()
