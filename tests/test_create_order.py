import requests
import json
import allure
import pytest
from urls import Urls
from data import TestData


class TestCreateOrder:

    @allure.description('Проверка возможности создания заказа самоката с выбором цвета: черный, серый, оба, не указан')
    @pytest.mark.parametrize('chosen_color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ''])
    def test_create_order_with_black_and_grey_color(self, chosen_color):
        TestData.order_data['color'] = [chosen_color]
        order_data_json = json.dumps(TestData.order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.url_create_order, data=order_data_json, headers=headers, timeout=5)
        assert response.status_code == 201 and 'track' in response.text
