# Flask Gallery

## Getting Started

The photo index can be stored in a json file, an sqlite db, Azure table storage or extended for your own db type. The default is to use the sqlite db. The record structure is as follows:

```json
{
  "objectID": "1",
  "imageUrl": "https://...",
  "thumbNail": "https:/...",
  "title": "Image A",
  "desc": "This is a photograph",
  "taken": "2018-01-01",
  "CRC": "0x7ED2A35C"
}
```           
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
