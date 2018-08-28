from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    instructions = models.TextField()
    ingredients = models.ManyToManyField('Ingredient', blank=True)

    def __str__(self):
        return self.title

    def is_vegetarian(self):
        for recipe_ingredient in self.ingredients.all():
            if recipe_ingredient.isMeat:
                return False

        return True


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    isMeat = models.BooleanField()
    recipes = models.ManyToManyField(Recipe, blank=True)

    def __str__(self):
        return self.name
