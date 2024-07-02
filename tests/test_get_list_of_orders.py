import requests
import allure
import pytest
from urls import Urls


class TestGetOrdersList:

    @allure.title('Проверка возможности получить список заказов')
    @allure.description('Тест проверяет, что в ответе приходит список, который содержит словари (заказы). '
                        'В каждом заказе есть id и track-номер')
    def test_get_list_of_orders(self):
        response = requests.get(Urls.url_get_orders_list)
        assert type(response.json()['orders']) == list and type(response.json()['orders'][0]) == dict
        assert "id", "track" in response.json()['orders'][0]
