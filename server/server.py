from functools import wraps
from flask import Flask, request, jsonify
from flask_cors import CORS
from db_connector import DB_Conector
#from flask_socketio import SocketIO
import fenixedu

app = Flask(__name__)
CORS(app)

#Initialize db connection
db = DB_Conector('asint')
token_dic = {}

def login_required(route_to_wrap):
    @wraps(route_to_wrap)
    def wrap(*args, **kwargs):
        info = request.get_json()
        
        if info:
            try:
                if info['token'] in list(token_dic.values()):
                    return route_to_wrap(*args, **kwargs)
                else:
                    return jsonify({'error': 'Permission denied!'}), 403

            except KeyError:
                return jsonify({'error': 'Permission denied!'}), 403
        else:
            return jsonify({'error': 'Permission denied!'}), 403

    return wrap


# ADMIN API
@app.route('/api/admin/login', methods = ['GET'])
def admin_login(): 
    login_info = request.get_json()
    if login_info:
        name = login_info['name']
        password = login_info['password']

        if name == 'admin' and password == '123':
            token_dic[name] = 'token_admin'
            return jsonify({'token': 'admin'}), 200
        else:
            return jsonify({'error': 'Wrong login information!'}), 400

    return jsonify({'error': 'No login information!'}), 400

@app.route('/api/admin/building', methods = ['POST'])
@login_required
def admin_add_building():
    building_info = request.get_json()
    
    if building_info:
        try:
            if building_info['type'] == 'CAMPUS': 
                result = db.addCampus(building_info)

            elif building_info['type'] == 'BUILDING':
                result = db.addBuilding(building_info)

            if result:
                return jsonify({'status': 'Successfull'}), 200
            else:
                return jsonify({'status': 'Could not perform this action, some inputs are invalid!'}), 400
        except KeyError:
            return jsonify({'status': 'Missing parameters!'}), 400
    else:
        return jsonify({'error': 'No building information!'}), 400

@app.route('/api/admin/building', methods = ['DELETE'])
@login_required
def admin_delete_building():
    building_info = request.get_json()
    
    try:
        if building_info:
            result = db.deleteSpace(building_info['spaceId'])
            if result:
                return jsonify({'status': 'Successfull'}), 200
            else:
                return jsonify({'status': 'Could not perform this action, space ID does not exists!'}), 400
        else:
            return jsonify({'error': 'No building information!'}), 400
    except KeyError:
        return jsonify({'status': 'Missing parameters!'}), 400

#USER API
@app.route('/api/user/login')
@login_required
def user_login():
    return 'user'

if __name__ == '__main__':
    app.run(debug = False)
