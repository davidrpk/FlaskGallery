from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET','OnceUponATimeThereWasAWickedWitchCalledNodeJS')