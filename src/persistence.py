class UserRepository:
    def __init__(self):
        self.users = []

    def get_users(self):
        return self.users

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def add_user(self, user):
        self.users.append(user)

    def update_user(self, user_id, user_data):
        for user in self.users:
            if user['id'] == user_id:
                user.update(user_data)
                return user
        return None

    def delete_user(self, user_id):
        self.users[:] = [user for user in self.users if user['id'] != user_id]
