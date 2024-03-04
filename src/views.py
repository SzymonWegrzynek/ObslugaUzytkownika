from flask import Flask
from flask import request
from flask import jsonify
from logic import UserLogic


app = Flask(__name__)

user_logic = UserLogic()


@app.get('/users')
def get_users():
    return jsonify(user_logic.get_all_users()), 200


@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = user_logic.get_specific_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.post('/users')
def create_user():
    user_data = request.get_json()
    user_logic.create_user(user_data)
    return jsonify(user_data), 201


@app.patch('/users/<int:user_id>')
def change_user_data(user_id):
    user_data = request.get_json()
    user = user_logic.change_user_data(user_id, user_data)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    user_logic.remove_user(user_id)
    return '', 204


if __name__ == "__main__":
    app.run("localhost", 8081, debug=True)
