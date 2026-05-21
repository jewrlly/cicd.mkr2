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

    def test_main_returns_max_10_recipes(self):
        response = self.client.get(reverse('main'))
        self.assertLessEqual(len(response.context['recipes']), 10)

class CategoryDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Soups")
        self.recipe = Recipe.objects.create(
            title="Borsch",
            description="Ukrainian soup",
            instructions="Cook it",
            ingredients="Beets, cabbage",
            category=self.category
        )

    def test_category_detail_returns_200(self):
        response = self.client.get(
            reverse('category_detail', kwargs={'pk': self.category.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_category_detail_uses_correct_template(self):
        response = self.client.get(
            reverse('category_detail', kwargs={'pk': self.category.pk})
        )
        self.assertTemplateUsed(response, 'category_detail.html')

    def test_category_detail_returns_404_for_invalid_id(self):
        response = self.client.get(
            reverse('category_detail', kwargs={'pk': 9999})
        )
        self.assertEqual(response.status_code, 404)