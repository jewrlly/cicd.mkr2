from django.test import TestCase, Client
from django.urls import reverse

from .models import Category, Recipe


class MainViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Desserts")
        for i in range(15):
            Recipe.objects.create(
                title=f"Recipe {i}",
                description=f"Description {i}",
                instructions=f"Instructions {i}",
                ingredients=f"Ingredients {i}",
                category=self.category
            )

    def test_main_returns_200(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_main_uses_correct_template(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'main.html')