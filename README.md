# Flask Gallery

#### Getting Started

data.json contains the index for all the photos. The JSON structure is as follows:

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
            

