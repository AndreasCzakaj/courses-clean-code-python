import unittest
from unittest import TestCase, skip, SkipTest
from parameterized import parameterized

from user_self_service.user_self_service import LoginService, User, LoginError, \
    UserDaoDictImpl


class LoginServiceTest(TestCase):

    def setUp(self):
        known_user = User()
        known_user.username = "known_user"
        self.database = UserDaoDictImpl({
            "known_user": known_user
        })
        self.service = LoginService(self.database)

    def test_login_should_fail_for_unknown_username(self):
        with self.assertRaises(LoginError):
            self.service.login({"userName": "unknown_user", "password": "correct_password"})

    def test_login_should_pass_for_correct_credentials(self):
        actual = self.service.login({"userName": "known_user", "password": "correct_password"})
        self.assertIsNotNone(actual)





if __name__ == '__main__':
    unittest.main()