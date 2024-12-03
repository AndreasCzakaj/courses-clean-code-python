import unittest
from unittest import TestCase
from parameterized import parameterized

from user_self_service import LoginService, Credentials, Dao, User, LoginError

class LoginServiceTest(TestCase):

    def setUp(self):
         existingUser = User()
         existingUser.email = "i_do_exist@test.com"
         existingUser.password = "right_password"
         self.existingUser = existingUser

         self.userDao = Dao[User]({
              existingUser.email: existingUser 
         })
         self.sut = LoginService(self.userDao)

    def test_fail_on_no_such_user(self): 
         # given
         credentials = Credentials()
         credentials.email = "i_do_not_exist@test.com"
         credentials.password = "123456"

         # then
         with self.assertRaisesRegex(LoginError, "No such user or wrong password"):
              self.sut.login(credentials)


if __name__ == '__main__':
    unittest.main()