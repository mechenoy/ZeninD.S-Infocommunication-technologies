
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_remote_ip():
    r = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY")
    jsondata = json.loads(r.text)
    photos = jsondata['photos']
    return render_template('index.html', photos=photos )

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)
