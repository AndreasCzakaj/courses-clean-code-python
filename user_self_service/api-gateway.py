# Small, single purpose, SRP class
class UserLogin:  
    def login():
        print("I'm doing some login stuff...")
        pass

# Small, single purpose, SRP class
class UserSignUp:  
    def signUp():
        print("I'm doing some signUp stuff...")
        pass


# API Gateway / Facade, givin access to the small classes
class UserSelfService:
    def __init__(self):
        self.login = UserLogin()
        self.signUp = UserSignUp()

    def login(self):
        self.login.login()

    def signUp(self):
        self.signUp.signUp()