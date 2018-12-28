from flask import Flask, render_template
from . import app
from . import photoindex


@app.route('/')
def index():
    photos = photoindex.fetchall()
    return render_template('index.html', photos=photos)


@app.route('/collection/<objectID>')
def collectionItem(objectID):
    record = photoindex.fetchone(objectID)
    if record is not None:
        return render_template('object.html', photo=record)
    return render_template('index.html')
