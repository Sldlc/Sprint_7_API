import requests
import allure
import pytest
from urls import Urls
from helpers import *
from data import TestData


class TestLoginCourier:

    @allure.title('Успешная аутентификация под валидными данными')
    def test_courier_login_with_valid_data(self):
        courier_payload = register_new_courier_with_static_data()
        response = requests.post(Urls.url_login_courier, data=courier_payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Неуспешная аутентификация при незаполненном поле логин или пароль')
    @pytest.mark.parametrize('fields', [
                             {'login': '', 'password': TestData.correct_password},
                             {'login': TestData.correct_login, 'password': ''},
                             ])
    def test_courier_login_with_empty_field(self, fields):
        response = requests.post(Urls.url_login_courier, data=fields)
        assert response.status_code == 400 and response.json() == {"message":  "Недостаточно данных для входа"}

    @allure.title('Неуспешная аутентификация под несуществующими данными')
    def test_courier_login_with_invalid_data(self):
        random_payload = {'login': generate_login(), 'password': generate_password()}
        response = requests.post(Urls.url_login_courier, data=random_payload)
        assert response.status_code == 404 and response.json() == {"message": "Учетная запись не найдена"}
