from persistence import UserRepository


class UserLogic:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_users(self):
        return self.user_repository.get_users()

    def get_specific_user(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def create_user(self, user_data):
        self.user_repository.add_user(user_data)

    def change_user_data(self, user_id, user_data):
        return self.user_repository.update_user(user_id, user_data)

    def remove_user(self, user_id):
        self.user_repository.delete_user(user_id)
