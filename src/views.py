from flask import Flask
from flask import request
from flask import jsonify
from logic import get_all_users
from logic import get_specific_user
from logic import create_user
from logic import change_user_data
from logic import remove_user


app = Flask(__name__)


@app.get('/users')
def get_users():
    return jsonify(get_all_users()), 200


@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = get_specific_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.post('/users')
def create_user():
    user_data = request.get_json()
    create_user(user_data)
    return jsonify(user_data), 201


@app.patch('/users/<int:user_id>')
def change_user_data(user_id):
    user_data = request.get_json()
    user = change_user_data(user_id, user_data)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    remove_user(user_id)
    return '', 204
