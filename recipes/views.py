from django.shortcuts import render, get_object_or_404

from .models import Recipe, Ingredient

def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}
    return render(request, "recipes/index.html", context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)

def ingredient_detail(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    context = {'ingredient': ingredient}
    return render(request, 'recipes/ingredient_detail.html', context)
