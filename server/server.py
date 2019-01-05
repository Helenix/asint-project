from flask import Flask, request, jsonify
from flask_cors import CORS
from db_connector import DB_Conector
import fenixedu

app = Flask(__name__)
CORS(app)

#Initialize db connection
db = DB_Conector('asint')
#db_users
#db_bots

# ADMIN API
@app.route('/api/admin/login', methods = ['GET'])
def admin_login(): 
    login_info = request.get_json()
    if login_info:
        name = login_info['name']
        password = login_info['password']

        if name == 'admin' and password == '123':
            # OK
            return jsonify({'token': 'admin'}), 200
        else:
            # Bad request
            return jsonify({'error': 'Wrong login information'}), 400
    # No content
    return jsonify({'error': 'No login information'}), 400

@app.route('/api/admin/building', methods = ['POST'])
def admin_add_building():
    building_info = request.get_json()
    if building_info:
        return jsonify({'status': 'successfull'}), 200
    else:
        return jsonify({'error': 'No building information'}), 400

#USER API
@app.route('/api/user/login')
def user_login():
    return 'user'

if __name__ == '__main__':
    app.run(debug = True)
