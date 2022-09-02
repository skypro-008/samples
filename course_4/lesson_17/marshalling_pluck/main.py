from flask import Flask
from flask_restx import fields, Api, marshal

app = Flask(__name__)
api = Api(app)

class User:
    """ Модель пользователя """
    def __init__(self, pk=0, name=None, city=None):
        self.pk = pk
        self.name = name
        self.city = city

class Order:
    """ Модель заказа """
    def __init__(self, pk=0, user=None):
        self.pk = pk
        self.user = user

# Создаем экземпляры объектов
default_user = User(pk=1, name="Алиса", city="Moscow")
default_order = Order(pk=1, user=default_user)

# Создаем модель для маршаллинга
order_api_model = api.model('Order', {
    'pk': fields.Integer,
    'user_pk': fields.Integer(attribute='user.pk'),
    'user_name': fields.String(attribute='user.name'),
    'city': fields.String(attribute='user.city'),
})

# Запускаем
output = marshal(default_order, order_api_model)
print(output)
