import requests
import json
import allure
import pytest
from urls import Urls
from data import TestData
from http import HTTPStatus


class TestCreateOrder:

    @allure.description('Проверка возможности создания заказа самоката с выбором цвета: черный, серый, оба, не указан')
    @pytest.mark.parametrize('chosen_color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ''])
    def test_create_order_with_black_and_grey_color(self, chosen_color):
        TestData.ORDER_DATA['color'] = [chosen_color]
        order_data_json = json.dumps(TestData.ORDER_DATA)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.URL_CREATE_ORDER, data=order_data_json, headers=headers, timeout=5)
        assert response.status_code == HTTPStatus.CREATED and 'track' in response.text
