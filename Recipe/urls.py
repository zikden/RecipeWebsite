from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="index"),
    path('recipes/', views.all_recipes, name="all_recipes"),
    path('my_recipe/', views.my_recipe, name="my_recipe"),
    path('recipe/<int:recipe_id>', views.recipe, name="recipe"),
]