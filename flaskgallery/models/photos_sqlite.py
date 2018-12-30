import sqlite3


class PhotoCollectionSQLite:
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
