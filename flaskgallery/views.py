from flask import Flask, render_template, request, abort, jsonify
from . import app
from . import photocollection
import json


@app.route('/')
def index():
    photos = photocollection.fetchall()
    return render_template('index.html', photos=photos)


@app.route('/collection/<objectID>')
def collectionItem(objectID):
    record = photocollection.fetchone(objectID)
    if record is not None:
        return render_template('object.html', photo=record)
    return render_template('index.html')


@app.route('/api/v1.0/collection/photos', methods=['POST'])
def add_photo():
    data = request.get_json()
    if not data:
        for record in data:
            if 'url' not in record['photo']:
                abort(400)
            photocollection.addone(record['photo'])
    return "{}", 201
