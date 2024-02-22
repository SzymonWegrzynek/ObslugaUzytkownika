users = []


def find_user_by_id(id):
    for user in users:
        if user['id'] == id:
            return user
    return None
