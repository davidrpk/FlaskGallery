# Flask Gallery

## Getting Started

data.json contains the index for all the photos. The JSON structure is as follows:

```json
{
  "objectID": "AA01",
  "imageUrl": "https://...",
  "thumbNail": "https:/...",
  "title": "Image A",
  "desc": "This is a photograph",
  "date": "5/10/2012"
}
```           
The 'read_photos()' function in our app file reads the data from this JSON file and passes it to the webpage requested.

You can access this information using for each photo by using a for loop in Jinja.

```html
{% for photo in photos %}
  <img src="{{photo.thumb}}" />
  <h4>{{photo.title}}</h4>
  <p>{{photo.year}}</p>
{% endfor %}
```
            
## Running

Windows:
```cmd
set FLASK_APP=flaskgallery.webapp
set FLASK_ENV=development
flask run
````
Unix/Mac:
```bash
export FLASK_APP=flaskgallery.webapp
export FLASK_ENV=development
flask run
```
