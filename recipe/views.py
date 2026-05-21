import random
from django.shortcuts import get_object_or_404, render

from .models import Category, Recipe


def main(request):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, min(10, len(recipes)))
    return render(request, 'main.html', {'recipes': random_recipes})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})
