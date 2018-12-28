from flask import Flask, render_template, request, abort, jsonify
from . import app
from . import photoindex
import json

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


@app.route('/api/v1.0/collection/photos', methods=['POST'])
def add_photo():
    data = request.get_json()
    if not data or 'url' not in data['photo']:
        abort(400)
    objectID = photoindex.addone(data['photo'])
    record = photoindex.fetchone(objectID)
    return jsonify(record), 201