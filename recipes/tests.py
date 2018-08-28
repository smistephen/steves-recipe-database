from django.test import TestCase

from .models import Recipe, Ingredient

class RecipeModelTests(TestCase):

    def test_is_vegetarian_with_vegetarian_recipe(self):
        """
        is_vegetarian() returns True for recipes containing
        no Ingredient objects for which isMeat is True.
        """
        vegetarian_recipe = Recipe(title="Test Recipe", instructions="Test the function")
        vegetarian_recipe.save()

        vegetarian_ingredient = Ingredient(name="Vegetarian Ingredient", isMeat=False)
        vegetarian_ingredient.save()

        vegetarian_recipe.ingredients.add(vegetarian_ingredient)

        self.assertIs(vegetarian_recipe.is_vegetarian(), True)

    def test_is_vegetarian_with_non_vegetarian_recipe(self):
        """
        is_vegetarian() returns False for recipes containing
        any Ingredient objects for which isMeat is True.
        """
        non_vegetarian_recipe = Recipe(title="Test Recipe", instructions="Test the function")
        non_vegetarian_recipe.save()

        non_vegetarian_ingredient = Ingredient(name="Non-Vegetarian Ingredient", isMeat=True)
        non_vegetarian_ingredient.save()

        non_vegetarian_recipe.ingredients.add(non_vegetarian_ingredient)

        self.assertIs(non_vegetarian_recipe.is_vegetarian(), False)
