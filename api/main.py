from flask import Flask, request 
import requests  
import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random/"
UNSPLASH_KEY= os.environ.get("UNSPLASH_KEY", "")

if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local file and nister the UNSPLASH_KEY there")
    
# UNSPLASH_KEY = "8lO7Sgx6euAg4LX18LzWl40GB-TnAu1cn8jxzSEg54g"




app = Flask(__name__)

@app.route("/newimg")
def newimg():
    word = request.args.get("query")
    print(word)
    # headers = {"Authorization" : "Client_ID"+UNSPLASH_KEY}
    params = {"query" : word,"client_id" : UNSPLASH_KEY}
    response = requests.get(url = UNSPLASH_URL,params=params)
    print(response.url)
    print(response)
    data = response.json()
    return  data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
