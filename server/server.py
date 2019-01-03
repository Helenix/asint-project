from flask import Flask, request, jsonify
from flask_cors import CORS
from tecnico_buildings import TecnicoBuildings
import fenixedu

app = Flask(__name__)
CORS(app)

tecnico = TecnicoBuildings("IST")
buildings = tecnico.getTecnico()

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
@app.route("/api/user/login")
def user_login():
    code = request.args['code']
    return jsonify({"code": code}), 200

if __name__ == "__main__":
    app.run(debug = True)
