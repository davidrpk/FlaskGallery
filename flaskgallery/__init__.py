from flask import Flask
import os
from flaskgallery.photostorage import SQLitePhotoIndex

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET',
                           'OnceUponATimeThereWasAWickedWitchCalledNodeJS')

photoindex = SQLitePhotoIndex('data/data.db')
