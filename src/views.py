from flask import Flask
from flask import jsonify


app = Flask(__name__)

users = []


@app.get('/users')
def get_users():
    return jsonify(users)


@app.get('/users/<int:id>')
def get_user(id):
    pass


@app.post('/users')
def create_user():
    pass


@app.patch('/users/<int:id>')
def change_user_data(id):
    user = requests.json
    users[id] = user
    return jsonify(user)


@app.delete('/users/<int:id>')
def delete_user(id):
    user = users.pop(id)
    return user
