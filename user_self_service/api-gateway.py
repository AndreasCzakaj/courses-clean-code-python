

class UserSelfService:
    def __init__(self):
        self.login = UserLogin()
        self.signUp = UserSignUp()

    def login(self):
        self.login.login()

    def signUp(self):
        self.signUp.signUp()


class UserLogin:  
    def login():
        pass

class UserSignUp:  
    def signUp():
        pass
