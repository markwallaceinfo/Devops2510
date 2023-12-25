from db_connector import connect_to_db
from db_connector import create_table
from flask import Flask, request

app = Flask(__name__)
user = create_table()


# supported methods
@app.route('/data/<user_id>', methods=['POST', 'GET', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, 200  # status code

    elif request.method == 'GET':
        request_data = request.json
       user_name = request_data.get(user_name)
        return {'status': 'ok', 'user_name': '<USER_NAME>'}, 200

    elif request.method == 'Put':

        return {}

    elif request.method == 'DELETE':

        return {}


# todo elif for put and delete


app.run(host='127.0.0.1', debug=True, port=5000)
