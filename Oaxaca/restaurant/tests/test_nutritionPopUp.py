import unittest
from restaurant.nutritionPopUp import item

class NutritionPopUpTest(unittest.TestCase):
    def test_initial_value(self):
        testObject = item("Dish", 281)
        
        self.assertEquals(testObject.public_attr_1, "Dish")
        self.assertEquals(testObject.public_attr_2, 281)