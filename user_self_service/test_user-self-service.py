import unittest
from unittest import TestCase, skip, SkipTest
from parameterized import parameterized

from user_self_service.user_self_service import LoginService, Credentials, UserDaoDictionaryImpl, User, LoginError

class LoginServiceTest(TestCase):

     def setUp(self):
         existingUser = User()
         existingUser.email = "i_do_exist@test.com"
         existingUser.password = "right_password"
         self.existingUser = existingUser

         self.userDao = UserDaoDictionaryImpl({
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

     @skip
     def test_fail_on_wrong_password(self):
        pass

     @skip
     def test_pass_if_email_and_password_correct(self):
        pass


if __name__ == '__main__':
    unittest.main()