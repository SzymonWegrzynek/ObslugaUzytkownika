from logic import get_all_users
from logic import get_specific_user
from logic import create_user
from logic import change_user_data
from logic import remove_user


def test_get_all_users():
    users = get_all_users()
    assert isinstance(users, list)


def test_get_specific_user():
    user = get_specific_user(1)
    assert user is None or isinstance(user, dict)


def test_create_user():
    user_data = {"id": 1, "name": "John"}
    create_user(user_data)
    assert get_specific_user(1) == user_data


def test_change_user_data():
    user_data = {"name": "Jane"}
    user = change_user_data(1, user_data)
    assert user is None or user['name'] == "Jane"


def test_remove_user():
    remove_user(1)
    assert get_specific_user(1) is None
