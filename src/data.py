class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru'


class WebEndpoints:
    MAIN_PAGE = '/'
    REGISTER_PAGE = '/register'
    LOGIN_PAGE = '/login'
    FORGOT_PASSWORD_PAGE = '/forgot-password'
    PROFILE_PAGE = '/account/profile'


class ApiEndpoints:
    REGISTER_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    USER = '/api/auth/user'


class TestData:
    VALID_PASSWORD_LENGTH = 6
    INVALID_PASSWORD_LENGTH = 5


class Texts:
    INVALID_PASSWORD_ERROR = 'Некорректный пароль'


def build_url(endpoint: str) -> str:
    return f'{Urls.BASE_URL}{endpoint}'
