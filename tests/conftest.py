import pytest
import sqlite3
import os


@pytest.fixture(scope='module')
def sqlite_connection():
    # TODO: setup test instance of db then destory after
    dbname = 'data/test_data.db'

    # TODO: check if db does not exist before continuing

    db = sqlite3.connect(dbname)
    sql_create_photos_table = """ CREATE TABLE IF NOT EXISTS `photos` (
                                        `objectID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                        `url` TEXT,
                                        `thumb` TEXT,
                                        `title` TEXT,
                                        `desc` TEXT
                                    ); """
    sql_create_photo_record = """ INSERT INTO `photos` (
                                        `url`,
                                        `thumb`,
                                        `title`,
                                        `desc`)
                                    VALUES (
                                        "https://s3-ap-southeast-2.amazonaws.com/flaskgallery-photos/600.png",
                                        "https://s3-ap-southeast-2.amazonaws.com/flaskgallery-photos/300.png",
                                        "Photo #1",
                                        "This is a description of the photograph"
                                    ); """
    
    c = db.cursor()
    c.execute(sql_create_photos_table)
    db.commit()
    c.execute(sql_create_photo_record)
    db.commit()

    db.close()

    yield dbname

    os.remove('data/test_data.db')


@pytest.fixture(scope='module')
def jsonfile_connection():
    dbname = 'data/test_data.json'
    return dbname
