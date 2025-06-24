from django.test import TestCase
from restaurant.models import MenuItem  

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        expected_str = "IceCream : 80" 
        self.assertEqual(str(item), expected_str)