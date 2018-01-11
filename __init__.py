from flask import Flask, render_template, url_for, redirect, request, flash, escape, session
from passlib.hash import sha256_crypt
import boto3
import json

app = Flask(__name__)

@app.route('/')
def index():
    photos = read_photos()
    return render_template('index.html', photos=photos)

def read_photos():
    # You can update this dictionary by change the attributes in 'data.json' file. An example of one row is given below
    #[{u'artist': u'John Smith', u'price': u'$250', u'title': u'img 001', u'source': u'../static/img/img.jpg', u'year': u'2012', u'desc': u'description'}]
    with open('data/data.json', 'r') as file:
        data = json.load(file, 'utf-8')
    return data

@app.route('/collection/<objectID>')
def collectionItem(objectID):

    # Dynamically route url to the photo that was selected.
    # This example opens new page and displays the photo with its information

    with open('data/data.json', 'r') as file:
        data = json.load(file, 'utf-8')

    for record in data:
        if record['objectID'] == objectID:
            return render_template('object.html', photo=record)

    return render_template('index.html')

app.secret_key = sha256_crypt.encrypt("big secret")

if __name__ == "__main__":
    app.debug = True
    app.run()
