from flask import Flask, render_template, url_for, redirect, request, flash, escape, session
from passlib.hash import sha256_crypt
import json
from . import app
from . import photoindex

@app.route('/')
def index():
    photos = photoindex.fetchall()
    return render_template('index.html', photos=photos)

@app.route('/collection/<objectID>')
def collectionItem(objectID):

    data = photoindex.fetchall()

    for record in data:
        if str(record['objectID']) == str(objectID):
            return render_template('object.html', photo=record)

    return render_template('index.html')
