from persistence import get_users
from persistence import get_user_by_id
from persistence import add_user
from persistence import update_user
from persistence import delete_user


def test_get_users():
    users = get_users()
    assert isinstance(users, list)


def test_get_user_by_id():
    user = get_user_by_id(1)
    assert user is None or isinstance(user, dict)


def test_add_user():
    user_data = {"id": 1, "name": "John"}
    add_user(user_data)
    assert get_user_by_id(1) == user_data


def test_update_user():
    user_data = {"name": "Jane"}
    user = update_user(1, user_data)
    assert user is None or user['name'] == "Jane"


def test_delete_user():
    delete_user(1)
    assert get_user_by_id(1) is None
