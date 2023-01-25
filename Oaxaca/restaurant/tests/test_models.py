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