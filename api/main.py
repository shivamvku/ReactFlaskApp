from distutils.debug import DEBUG
from flask import Flask, request 
import requests  
import os 
from dotenv import load_dotenv
from flask_cors import CORS


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
    print(word)
    # headers = {"Authorization" : "Client_ID"+UNSPLASH_KEY}
    params = {"query" : word,"client_id" : UNSPLASH_KEY}
    response = requests.get(url = UNSPLASH_URL,params=params)
    print(response)
    data = response.json()
    return  data

# @app.route("/images")
# def images():

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
