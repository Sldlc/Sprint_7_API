import random
import string
from faker import Faker


fake = Faker()


def generate_login():
    log = fake.text(10)
    login = log[:-1]
    return login


def generate_password():
    password = fake.password(length=8, digits=True)
    return password


def generate_first_name():
    first_name = fake.first_name()
    return first_name


def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(8)
    first_name = generate_random_string(6)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


def register_new_courier_with_static_data():
    payload = {
        "login": 'Saymyo',
        "password": '123456',
        "firstName": 'Samuel'
    }
    return payload

