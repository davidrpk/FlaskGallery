from flaskgallery.photostorage import PhotoIndex, SQLitePhotoIndex, JSONPhotoIndex
import tests.conftest


def test_sqlite_connection(sqlite_connection):
    db = SQLitePhotoIndex(sqlite_connection)
    # TODO: add method to db to perform db check rather than fetch all
    records = db.fetchall()
    assert len(records) > 0


def test_jsonfile_connection(jsonfile_connection):
    db = JSONPhotoIndex(jsonfile_connection)
    records = db.fetchall()
    assert len(records) > 0