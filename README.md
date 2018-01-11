# Flask Gallery
###### The easiest way to dynamically load images into your flask web application 
###### https://flaskgallery.com/


#### Getting Started


Firstly, we need to store our images in an Amazon Web Services S3 Bucket (You can also store images in the local directory, all you need to do is copy the url into the JSON file).

We can update the JSON file to contain different attributes related to each photo.

`{
              "objectID": "AA01",
              "imageUrl": "https://...",
              "thumbNail": "https:/...",
              "title": "Image A",
              "desc": "This is a photograph",
              "date": "5/10/2012"
            }`
            


The 'read_photos()' function in our app file reads the data from this JSON file and passes it to the webpage requested.

You can access this information using for each photo by using a for loop in Jinja.

`    {% for photo in photos %}
                  <img src="{{photo.thumb}}" />
                  <h4>{{photo.title}}</h4>
                  <p>{{photo.year}}</p>
                {% endfor %}`
            





#### Tasks

[x] Reading data from s3 bucket

[x] Basic dynamic routing

[ ] Upload to s3 bucket

[ ] Manage photos in a bucket (edit attributes, delete)

[ ] Password secure login to upload photos


##### Developers - please fork and make a pull request, include comments in your work so people can understand your code



###### Donate Bitcoin: 1CUz6mRsZTp3cK55bhQF5kJiUtBWqjB9ML 
