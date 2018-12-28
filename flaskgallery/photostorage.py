import sqlite3
import json


class PhotoIndex:
    def __init__(self):
        print('')

    def fetchall(self):
        raise NotImplementedError()

    def fetchone(self, objectID):
        raise NotImplementedError()

    def addone(self, photo):
        raise NotImplementedError()


class SQLitePhotoIndex:
    _dblocation = ''

    def __init__(self, dblocation):
        self._dblocation = dblocation

    def fetchall(self):
        db = sqlite3.connect(self._dblocation)
        db.row_factory = sqlite3.Row
        c = db.cursor()
        c.execute('''SELECT * FROM photos''')
        rows = c.fetchall()
        photos = []
        for row in rows:
            photo = dict(zip(row.keys(), row))
            photos.append(photo)
        db.close()
        return photos

    def fetchone(self, objectID):
        db = sqlite3.connect(self._dblocation)
        db.row_factory = sqlite3.Row
        c = db.cursor()
        intObjectID = 0
        try:
            intObjectID = int(objectID)
        except ValueError:
            return None
        c.execute('''SELECT * FROM photos WHERE objectID=?''', (intObjectID,))
        row = c.fetchone()
        if row is not None:
            photo = dict(zip(row.keys(), row))
            return photo

    def addone(self, photo):
        db = sqlite3.connect(self._dblocation)
        c = db.cursor()

        sql = """ INSERT INTO `photos` (
                        `url`,
                        `thumb`,
                        `title`,
                        `desc`)
                    VALUES (
                        ?,
                        ?,
                        ?,
                        ?
                    ); """

        print(photo.values())
        c.execute(sql, tuple(photo.values()))
        db.commit()
        objectID = c.lastrowid
        return objectID


class JSONPhotoIndex:
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
