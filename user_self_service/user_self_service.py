from abc import ABC, abstractmethod
from typing import Protocol


class UserSelfServiceError(ABC, Exception):
    def __init__(self, message):
        super().__init__(message)

class LoginError(UserSelfServiceError):
    def __init__(self, message):
        super().__init__(message)

class User:
    def __init__(self):
        self.username = ""
        self.password = ""

class UserDao(Protocol):
    def get(self, identifier: str) -> User | None:
        ...

class UserDaoDictImpl(UserDao):
    def __init__(self, repo: dict = {}):
        self.repo = repo

    def get(self, identifier: str) -> User | None:
        return self.repo.get(identifier, None)


class LoginService:
    def __init__(self, user_dao: UserDao):
        self._user_dao = user_dao

    def login(self, credentials: dict):
      user = self._user_dao.get(credentials["userName"])
      if user is None:
        raise LoginError("unknown user or wrong password")

      return {}

        


    