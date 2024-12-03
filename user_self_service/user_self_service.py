from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')  # Define type variable "T"

class UserSelfServiceError(ABC, Exception):
    def __init__(self, message):
        super().__init__(message)

class LoginError(UserSelfServiceError):
    def __init__(self, message):
        super().__init__(message)


class Dao(Generic[T]):
    def __init__(self, repo = {}):
        self.repo = repo

    def get(self, identifier: str) -> T:
        if identifier in self.repo:
            return self.repo.get(identifier)
        return None

    def save(self, identifier: str, data: T) -> T:
        self.repo[identifier] = data
        return data


class User:
    email: str
    password: str

class Credentials:
    email: str
    password: str

class UserSession:
    id: str


class LoginService:
    def __init__(self, userDao: Dao[User]) -> None:
        self.userDao = userDao

    def login(self, credentials: Credentials) -> UserSession:
        pass


    