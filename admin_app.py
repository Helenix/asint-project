#token = admin
import getpass
import requests
import json

name = input("Login name: ")
password = getpass.getpass("Password: ")

payload = {
    "name": name,
    "password": password
}

url = "http://127.0.0.1:5000/"

response = requests.post(url + "admin/login", json = payload)

print(response.status)
