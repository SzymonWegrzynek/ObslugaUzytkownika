from persistence import get_users
from persistence import get_user_by_id
from persistence import add_user
from persistence import update_user
from persistence import delete_user


def get_all_users():
    return get_users()


def get_specific_user(user_id):
    return get_user_by_id(user_id)


def create_user(user_data):
    add_user(user_data)


def change_user_data(user_id, user_data):
    return update_user(user_id, user_data)


def remove_user(user_id):
    delete_user(user_id)
