from flaskgallery.models.photos_jsonfile import PhotoCollectionJSONFile
from flaskgallery.models.photos_sqlite import PhotoCollectionSQLite
import tests.conftest


def test_sqlite_connection(sqlite_connection):
    db = PhotoCollectionSQLite(sqlite_connection)
    # TODO: add method to db to perform db check rather than fetch all
    records = db.fetchall()
    assert len(records) > 0


def test_sqlite_add_one(sqlite_connection):
    db = PhotoCollectionSQLite(sqlite_connection)
    photo = {"url": "https://s3-ap-southeast-2.amazonaws.com/flaskgallery-photos/600.png",
             "thumb": "https://s3-ap-southeast-2.amazonaws.com/flaskgallery-photos/300.png",
             "title": "Photo #3",
             "desc": "This is a description of the photograph"}
    objectID = db.addone(photo)
    photo['objectID'] = objectID
    # TODO: remove dependency on fetchone to catch regressions effecting both
    photo_read = db.fetchone(objectID)
    assert photo == photo_read


def test_jsonfile_connection(jsonfile_connection):
    db = PhotoCollectionJSONFile(jsonfile_connection)
    records = db.fetchall()
    assert len(records) > 0