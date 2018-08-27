from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('ingredient/<int:ingredient_id>/', views.ingredient_detail, name='ingredient_detail'),
]
