from flask import Flask
import os
from .models.photos_azuretable import PhotoCollectionAzureTable
from .models.photos_sqlite import PhotoCollectionSQLite
from .models.photos_jsonfile import PhotoCollectionJSONFile

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET',
                           'OnceUponATimeThereWasAWickedWitchCalledNodeJS')

# SQLite
photocollection = PhotoCollectionSQLite('data/data.db')

# Azure Table Storage
# connection_string = os.getenv('STORAGE_CONNECTION_STRING',
#                              '')
# photocollection = PhotoCollectionAzureTable(connection_string)

# JSON file
# photo collection = PhotoCollectionJSONFile('data/data.json')
