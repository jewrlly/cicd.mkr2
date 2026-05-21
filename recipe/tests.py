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
