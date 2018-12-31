from flask import Flask, render_template, request, abort, jsonify
from . import app
from . import photocollection


@app.route('/')
def index():
    photos = photocollection.fetchall()
    return render_template('index.html', photos=photos)


@app.route('/collection/photos/<objectID>')
def collectionItem(objectID):
    record = photocollection.fetchone(objectID)
    if record is not None:
        return render_template('object.html', photo=record)
    return render_template('index.html')


@app.route('/api/v1.0/collection/photos', methods=['POST'])
def add_photo():
    data = request.get_json()
    if data is not None:
        for record in data:
            if 'url' not in record['photo']:
                abort(400)
            photocollection.addone(record['photo'])
    return "{}", 201


@app.route('/api/v1.0/collection/photos/<objectID>', methods=['GET'])
def get_photo(objectID):
    photos = photocollection.fetchone(objectID)
    return jsonify(photos), 200
