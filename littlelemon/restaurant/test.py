from django.test import TestCase
from .models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream : $80')
        
        
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title='IceCream', price='80.00', inventory=100)
        Menu.objects.create(title='Burger', price='10.00', inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        items = Menu.objects.all()
        serialized = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized.data)