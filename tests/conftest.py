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
                                        `objectID` TEXT NOT NULL UNIQUE,
                                        `url` TEXT,
                                        `thumb` TEXT,
                                        `title` TEXT,
                                        `desc` TEXT,
                                        `taken` TEXT,
                                        `CRC` TEXT,
                                        PRIMARY KEY(`objectID`)
                                    ); """
    sql_create_photo_record = """ INSERT INTO `photos` (
                                        `objectID`,
                                        `url`,
                                        `thumb`,
                                        `title`,
                                        `desc`,
                                        `taken`,
                                        `CRC`)
                                    VALUES (
                                        "96de6a68-4fc2-411c-91a3-52ae37879481",
                                        "https://s3-ap-southeast-2.amazonaws.com/flaskgallery-photos/600.png",
                                        "https://s3-ap-southeast-2.amazonaws.com/flaskgallery-photos/300.png",
                                        "Photo #1",
                                        "This is a description of the photograph",
                                        "2018-01-01",
                                        "0x784DD132"
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
