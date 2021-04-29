class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_credentials(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False