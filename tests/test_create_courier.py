import requests
import allure
import pytest
from data import TestData
from helpers import *
from urls import Urls
from http import HTTPStatus



class TestCreateCourier:
    @allure.title('Успешное создание аккаунта курьера с валидными данными')
    def test_create_courier_account_created(self):
        courier_payload = register_new_courier_and_return_login_password()
        response = requests.post(Urls.URL_CREATE_COURIER, data=courier_payload)
        assert response.status_code == HTTPStatus.CREATED and response.json() == {'ok': True}

    @allure.title('Неуспешное создание курьера с теми же данными, введенными повторно')
    def test_create_duplicate_courier(self):
        courier_payload = register_new_courier_with_static_data()
        requests.post(Urls.URL_CREATE_COURIER, data=courier_payload)
        second_response = requests.post(Urls.URL_CREATE_COURIER, data=courier_payload)
        assert (second_response.status_code == HTTPStatus.CONFLICT and
                second_response.json() == TestData.MESSAGE_CONFLICT)

    @allure.title('Попытка создать курьера с одним незаполненным полем. Ожидаем 400 везде.')
    @pytest.mark.parametrize('fields', [
                             {'login': '', 'password': generate_password(), 'firstName': generate_first_name()},
                             {'login': generate_login(), 'password': '', 'firstName': generate_first_name()},
                             {'login': generate_login(), 'password': generate_password(), 'firstName': ''}
                             ])
    def test_create_courier_with_empty_field(self, fields):
        response = requests.post(Urls.URL_CREATE_COURIER, data=fields)
        assert (response.status_code == HTTPStatus.BAD_REQUEST and
                response.json() == TestData.MESSAGE_BAD_REQUEST)
