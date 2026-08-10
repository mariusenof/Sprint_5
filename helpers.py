import random
import string


def generate_email():
    random_number = random.randint(100, 999)

    return f'nikita_egorov_51_{random_number}@yandex.ru'


def generate_password(length=8):
    characters = string.ascii_letters + string.digits

    return ''.join(
        random.choice(characters)
        for _ in range(length)
    )