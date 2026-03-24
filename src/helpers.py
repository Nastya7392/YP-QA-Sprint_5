import random
import string

from faker import Faker

from src.data import TestData

fake = Faker(['ru_RU'])


def generate_name() -> str:
    return fake.name()


def generate_login() -> str:
    return fake.free_email()


def generate_password(length: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_valid_password() -> str:
    return generate_password(TestData.VALID_PASSWORD_LENGTH)


def generate_invalid_password() -> str:
    return generate_password(TestData.INVALID_PASSWORD_LENGTH)


def generate_user_payload() -> dict:
    return {
        'email': generate_login(),
        'password': generate_valid_password(),
        'name': generate_name(),
    }
