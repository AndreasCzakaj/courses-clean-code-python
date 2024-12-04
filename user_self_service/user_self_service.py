from abc import ABC, abstractmethod

class UserSelfServiceError(ABC, Exception):
    def __init__(self, message):
        super().__init__(message)

class LoginError(UserSelfServiceError):
    def __init__(self, message):
        super().__init__(message)


class DataAccessObject(ABC):
    @abstractmethod
    def get(self, identifier: str):
        pass


class User:
    email: str
    password: str

class UserDaoDictionaryImpl(DataAccessObject):
    def __init__(self, repo = {}):
        self.repo = repo

    def get(self, identifier: str) -> User:
        if identifier in self.repo:
            return self.repo.get(identifier)
        return None

    #def save(self, identifier: str, data: User) -> User:
    #    self.repo[identifier] = data
    #    return data



class Credentials:
    email: str
    password: str

class UserSession:
    id: str


class LoginService:
    def __init__(self, userDao: DataAccessObject) -> None:
        self.userDao = userDao

    def login(self, credentials: Credentials) -> UserSession:
        user = self.userDao.get(credentials.email)
        if user == None:
            raise LoginError("No such user or wrong password")
        


    