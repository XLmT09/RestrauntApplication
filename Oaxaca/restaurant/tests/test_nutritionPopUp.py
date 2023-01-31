import unittest
from restaurant.nutritionPopUp import item

class NutritionPopUpTest(unittest.TestCase):
    def test_initial_value(self):
        testObject = item("Dish", 281)
        
        self.assertEquals(testObject.public_attr_1, "Dish")
        self.assertEquals(testObject.public_attr_2, 281)
    
    def test_values1(self):
        testObject = item("Another dish", 188)

        self.assertEquals(testObject.public_attr_1, "Another dish")
        self.assertEquals(testObject.public_attr_1, "188")

    def test_values2(self):
        testObject = item("Dish", 281)

        self.assertNotEquals(testObject.public_attr_1, "Another dish")
        self.assertEquals(testObject.public_attr_2, 281)