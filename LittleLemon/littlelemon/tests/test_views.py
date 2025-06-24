from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

        self.item1 = MenuItem.objects.create(title="Pizza", price=12.50, inventory=5)
        self.item2 = MenuItem.objects.create(title="Burger", price=8.00, inventory=3)

    def test_getall(self):
        response = self.client.get('/menu/')
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)