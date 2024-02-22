users = []


def get_users():
    return users


def get_user_by_id(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None


def add_user(user):
    users.append(user)


def update_user(user_id, user_data):
    for user in users:
        if user['id'] == user_id:
            user.update(user_data)
            return user
    return None


def delete_user(user_id):
    users[:] = [user for user in users if user['id'] != user_id]
