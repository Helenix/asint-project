#from flask import Flask

#app = Flask(__name__)

#if __name__ == "__main__":
#    app.run(debug = True)
import requests
import json

url = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces/2448131392438"

response = requests.get(url)
print(response.text)