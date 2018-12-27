import sqlite3
import json

class PhotoIndex:
    def __init__(self):
        print('')
    def fetchall(self):
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

class JSONPhotoIndex:
    def fetchall(self):
        with open('data/data.json', 'r') as file:
            data = json.load(file)
        return data