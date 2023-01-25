from django.test import TestCase
from django.urls import reverse

#Test views (Uses Reverse)

class HomePageTest(TestCase):
    def test_restaurant_view1(self):
        menuItem = self.create_MenuItem()
        url = reverse("restaurant.views.homePage")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(menuItem.title, response.content)

    def test_restaurant_view2(self):
        order = self.create_Order()
        url = reverse("restaurant.views.homePage")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(order.title, response.content)

class MenuTest(TestCase):
    def test_restaurant_menu1(self):
        menuItem = self.create_MenuItem()
        url = reverse("restaurant.views.menu")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(menuItem.title, response.content)

    def test_restaurant_menu2(self):
        order = self.create_Order()
        url = reverse("restaurant.views.menu")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(order.title, response.content)