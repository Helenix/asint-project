from flask import Flask, request, jsonify
import time
from istdb import ISTdb

app = Flask(__name__)

tecnico = ISTdb("ISTdb")
db = tecnico.getDB()

@app.route("/")
def root():
    return "root"

@app.route("/api/admin/login", methods = ["GET"])
def admin_login(): 
    login_info = request.get_json()
    if login_info:
        name = login_info["name"]
        password = login_info["password"]

        if name == "admin" and password == "admin123":
            # OK
            return jsonify({"token": "admin"}), 200
        else:
            # Bad request
            return jsonify({"error": "Wrong login informatarion"}), 400
    # No content
    return jsonify({"error": "No login information"}), 400
    

if __name__ == "__main__":
    app.run(debug = True)
