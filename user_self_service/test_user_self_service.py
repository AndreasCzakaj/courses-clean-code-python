# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

import pytest
from user_self_service import SignUpData, SignUpService, SignUpError, UserSession, LoginService, Credentials, UserDaoDictionaryImpl, User, LoginError

existingUser = None
userDao = None

class Fixture:
    existingUser: User
    loginService: LoginService
    signUpService: SignUpService

@pytest.fixture
def fixture():    
    existingUser = User()
    existingUser.email = "i_do_exist@test.com"
    existingUser.password = "right_password"

    userDao = UserDaoDictionaryImpl({
        existingUser.email: existingUser 
    })

    out = Fixture()
    out.existingUser = existingUser
    out.loginService = LoginService(userDao)
    out.signUpService = SignUpService(userDao)

    return out


def test_fail_on_no_such_user(fixture: Fixture):
    service = fixture.loginService
    credentials = Credentials()
    credentials.email = "i_do_not_exist@test.com"
    credentials.password = "123456"

    with pytest.raises(LoginError, match="No such user or wrong password"):
        service.login(credentials)


def test_fail_on_wrong_password(fixture: Fixture):
    service = fixture.loginService
    credentials = Credentials()
    credentials.email = fixture.existingUser.email
    credentials.password = "wrong_password"

    with pytest.raises(LoginError, match="No such user or wrong password"):
        service.login(credentials)


def test_pass_on_correct_credentials(fixture: Fixture):
    service = fixture.loginService
    credentials = Credentials()
    credentials.email = fixture.existingUser.email
    credentials.password = fixture.existingUser.password

    actual = service.login(credentials)

    assert actual != None
    assert isinstance(actual, UserSession)


def test_fail_on_duplicate(fixture: Fixture):
    service = fixture.signUpService
    data = SignUpData()
    data.email = fixture.existingUser.email

    with pytest.raises(SignUpError, match="Email already taken"):
        service.signUp(data)


def test_fail_on_invalid_email(fixture: Fixture):
    service = fixture.signUpService
    data = create_minimal_valid_SignUpData()
    data.email = data.email[:-1]

    with pytest.raises(SignUpError, match="invalid email"):
        service.signUp(data)

def create_minimal_valid_SignUpData():
    data = SignUpData()
    data.email = "test@test.de"
    data.password = "12345678"
    return data

