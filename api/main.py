from distutils.debug import DEBUG
from flask import Flask, request, jsonify
import requests  
import os 
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import mongo_client

gallery = mongo_client.gallery
img_coll = gallery.images

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random/"
UNSPLASH_KEY= os.environ.get("UNSPLASH_KEY", "")
DEBUG=bool(os.environ.get("DEBUG", True))
if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local file and nister the UNSPLASH_KEY there")
    

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = DEBUG


@app.route("/newimg")
def newimg():
    word = request.args.get("query")
    # return {'word':word}
    print(word)
    # headers = {"Authorization" : "Client_ID"+UNSPLASH_KEY}
    params = {"query" : word,"client_id" : UNSPLASH_KEY}
    response = requests.get(url = UNSPLASH_URL,params=params)
    print(response)
    data = response.json()
    return  data

@app.route("/images", methods=["GET","POST"])
def images():
    if request.method == "GET":
        images = img_coll.find({})
        return jsonify([img for img in images])
    if request.method == "POST":
        img = request.get_json()
        img["_id"] = img.get("id")
        result = img_coll.insert_one(img)
        inserted_id = result.inserted_id

        return {"inserted_id": inserted_id}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
