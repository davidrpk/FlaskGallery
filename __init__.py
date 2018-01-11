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

@app.route('/login', methods=["POST"])
def login():
	error = ""

	try:
		if request.method == 'POST':
			email = request.form['email']
			pw = request.form['password']

			if email == 'test@test.com':
				session['admin'] = True

				return redirect(url_for("admin"))

			else:
				error = "Unsuccessful login."

		return render_template('admin.html', error=error)

	except Exception as e:
		return render_template('login.html', error=error)

@app.route('/upload', methods=['GET', 'POST'])
def upload():

    error=""

    client = boto3.client('s3')

    if request.method == 'GET':
        typeofaction = request.args.get('type')
        filename = request.args.get('filename')

        if typeofaction == 'delete':
            client.delete_object(Bucket='zappa-flowers', Key=filename)

        else:
            return render_template('admin.html', files=[])

    elif request.method == 'POST':
        # load 2 images, high resolution and low resolution
        highRes = request.files.get('file')
        thumb = request.files.get('thumb')

        client.put_object(Bucket='zappa-flowers', Body=highRes.read(), Key=highRes.filename)
        client.put_object(Bucket='zappa-flowers', Body=thumb.read(), Key=thumb.filename)


        objectID = request.args.get('objectID')
        filename = request.args.get('filename')
        paypalID = request.args.get('paypalID')
        title = request.args.get('filename')

        # load photos data
        with open('data/data.json', 'r') as f:
            data = json.loads(f.read())
        for record in data:
            print record

        new_record = json.dumps({"objectID": ""})

        # client.put_object(Bucket='zappa-flowers', Body=x.read(), Key=x.filename)

        return render_template('admin.html', session=session, files=client.list_objects_v2(Bucket='zappa-flowers'))

    else:
        return render_template('admin.html', error='No Admin Session Found.')

app.secret_key = sha256_crypt.encrypt("big secret")

if __name__ == "__main__":
    app.debug = True
    app.run()
