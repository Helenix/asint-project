from functools import wraps
from flask import Flask, request, jsonify
from flask_cors import CORS
from db_connector import DB_Conector
import fenixedu
from random import randint

app = Flask(__name__)
CORS(app)

#Initialize db connection
db = DB_Conector('asint')
token_dic = {}

# IR BUSCAR AO HEADER AUTHORIZATION EM VEZ DE ENVIAR JSON
def user_login_required(route_to_wrap):
    @wraps(route_to_wrap)
    def wrap(*args, **kwargs):
        info = request.get_json()
        
        if info:
            try:
                if info['token'] in list(token_dic.values()) and info['token'] != token_dic['admin']:
                    return route_to_wrap(*args, **kwargs)
                else:
                    return jsonify({'error': 'Permission denied!'}), 403

            except KeyError:
                return jsonify({'error': 'Permission denied!'}), 403
        else:
            return jsonify({'error': 'Permission denied!'}), 403

    return wrap

def admin_login_required(route_to_wrap):
    @wraps(route_to_wrap)
    def wrap(*args, **kwargs):
        info = request.get_json()
        
        if info:
            try:
                if info['token'] in list(token_dic.values()) and info['token'] == token_dic['admin']:
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
        try:
            name = login_info['name']
            password = login_info['password']

            if name == 'admin' and password == '123':
                if 'admin' not in list(token_dic.keys()):
                    token_dic[name] = 'token_admin_' + str(randint(10000000,100000000))
                    return jsonify({'token': token_dic[name]}), 200
                else:
                    return jsonify({'error': 'User already logged!'}), 400
            else:
                return jsonify({'error': 'Wrong login information!'}), 400
        except KeyError:
             return jsonify({'error': 'Wrong format!'}), 400
    return jsonify({'error': 'No login information!'}), 400

@app.route('/api/admin/logout', methods = ['GET'])
@admin_login_required
def admin_logout():
    logout_info = request.get_json()

    if logout_info:
        try:
            token = logout_info['token']
            if token in list(token_dic.values()):
                token_dic.pop('admin')
                return jsonify({'status': 'Successfull logout!'}), 200
        except KeyError:
             return jsonify({'error': 'Wrong format!'}), 400
    return jsonify({'error': 'No parameters!'}), 400

@app.route('/api/admin/building', methods = ['POST'])
@admin_login_required
def admin_add_building():
    building_info = request.get_json()
    building_info.pop('token')
    
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
@admin_login_required
def admin_delete_building():
    building_info = request.get_json()
    building_info.pop('token')
    
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

@app.route('/api/admin/logs', methods = ['GET'])
@admin_login_required
def admin_get_logs():
    result = db.getLogs()
    return jsonify(result)
#USER API
@app.route('/api/user/login')
@user_login_required
def user_login():
    return 'user'

#BOT API
@app.route('/api/bot/login', methods = ['GET'])
def bot_login():
    acc_info = request.get_json()
    
    if acc_info:
        result = db.authenticateBot(acc_info)
        if result:
            return jsonify({'token': 'bot_token'}), 400
        else:
            return jsonify({'error': 'Login failled!'}), 400
    else:
        return jsonify({'error': 'No bot account information!'}), 400

@app.route('/api/bot/account', methods = ['POST'])
def bot_account_creation():
    acc_info = request.get_json()

    if acc_info:
        result = db.addBot(acc_info)
        if result:
            return jsonify({'status': 'Bot created'}),200
        else:
            return jsonify({'status': 'Something already in use'}),400
    else:
        return jsonify({'error': 'No bot account information!'}), 400


if __name__ == '__main__':
    app.run(debug = False)
