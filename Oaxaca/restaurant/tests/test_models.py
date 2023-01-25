from django.test import TestCase
from restaurant.models import MenuItem
from django.utils import timezone
from django.urls import reverse

# Test models

class MenuItemTest(TestCase):
	def create_MenuItem(self, ID = 1, name = 'Dish', price = 6.99, calories = 281, cuisine = 'Mexican', ingredients = ['A', 'B'], dietRequirements = 'Vegan'):
		return MenuItem.objects.create(ID = ID, name = name, price = price, calories = calories, cuisine = cuisine, ingredients = ingredients, dietRequirements = dietRequirements)

	def test_MenuItem_creation(self):
		menuItem = self.create_menuItem()
		self.assertTrue(isinstance(menuItem, MenuItem))

class OrderTest(TestCase): 
    def create_Order(self, ID = 1, customerID = 2, status = 'Placed', timeOfOrder = '2023-01-25' '18:21:48', orderedItems = ['Dish', 'Another dish']):
        return Order.objects.create(ID = ID, customerID = customerID, status = status, timeOfOrder = timeOfOrder, orderedItems = orderedItems)
    
    def test_Order_creation(self):
        order = self.create_Order()
        self.assertTrue(isinstance(order, Order))