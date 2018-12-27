import sqlite3
import json

class PhotoIndex:
    def __init__(self):
        print('')
    def fetchall(self):
        raise NotImplementedError()
    def fetchone(self,objectID):
        raise NotImplementedError()

class SQLitePhotoIndex:
    def fetchall(self):
        db = sqlite3.connect('data/data.db')
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
    def fetchone(self,objectID):
        db = sqlite3.connect('data/data.db')
        db.row_factory = sqlite3.Row
        c = db.cursor()
        c.execute('''SELECT * FROM photos WHERE objectID=?''',(objectID,))
        row = c.fetchone()
        if row != None:
            photo = dict(zip(row.keys(), row))
            return photo

        return None

class JSONPhotoIndex:
    def fetchall(self):
        with open('data/data.json', 'r') as file:
            data = json.load(file)
        return data
    def fetchone(self,objectID):
        for record in self.fetchall():
            if str(record['objectID']) == str(objectID):
                return record
        return None
