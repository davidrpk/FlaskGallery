import sqlite3
import uuid

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
        # TODO: sanitize objectID input
        c.execute("""SELECT * FROM photos WHERE objectID=?""", (objectID,))
        row = c.fetchone()
        if row is not None:
            photo = dict(zip(row.keys(), row))
            return photo

    def addone(self, photo):
        db = sqlite3.connect(self._dblocation)
        c = db.cursor()
        objectID = str(uuid.uuid4())
        sql = """ INSERT INTO `photos` (
                        `objectID`,
                        `url`,
                        `thumb`,
                        `title`,
                        `desc`,
                        `taken`,
                        `CRC`)
                    VALUES (
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?
                    ); """

        c.execute(sql, (
            objectID,
            photo['url'],
            photo['thumb'],
            photo['title'],
            photo['desc'],
            photo['taken'],
            photo['CRC']
        ))
        db.commit()
        return objectID
