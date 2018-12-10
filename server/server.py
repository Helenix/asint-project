from flask import Flask, request, jsonify
from flask_cors import CORS
import time
from istdb import ISTdb

app = Flask(__name__)
CORS(app)

tecnico = ISTdb("ISTdb")
db = tecnico.getDB()

@app.route("/")
def root():
    return "root"

# ADMIN API
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

#USER API
@app.route("/api/user", methods = ["GET"])
def user_root():
    response = jsonify({"message": "Hey user"})

    return jsonify({"message": "Hey user"}), 200
    

if __name__ == "__main__":
    app.run(debug = True)
