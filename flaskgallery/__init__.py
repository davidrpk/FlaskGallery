from flask import Flask
import os
from .models.photos_sqlite import PhotoCollectionSQLite

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET',
                           'OnceUponATimeThereWasAWickedWitchCalledNodeJS')

photocollection = PhotoCollectionSQLite('data/data.db')
