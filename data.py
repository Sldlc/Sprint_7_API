
class TestData:

    CORRECT_LOGIN = "Frimpong"
    CORRECT_PASSWORD = "4321"
    CORRECT_NAME = "Jordan"

    ORDER_DATA = {
                "firstName": "Naruto",
                "lastName": "Uchiha",
                "address": "Konoha, 142 apt.",
                "metroStation": 4,
                "phone": "+7 800 355 35 35",
                "rentTime": 5,
                "deliveryDate": "2020-06-06",
                "comment": "Saske, come back to Konoha"
                }

    MESSAGE_CONFLICT = {"message": "Этот логин уже используется"}
    MESSAGE_BAD_REQUEST = {"message": "Недостаточно данных для создания учетной записи"}
    MESSAGE_NOT_FOUND = {"message": "Учетная запись не найдена"}

