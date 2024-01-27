from django.shortcuts import get_object_or_404, render

from .models import Recipe, Ingredient

# user = 

def main_page(request):
    context = {
        "title": "Главная",
    }
    return render(request, "Recipe/main.html", context=context)

def all_recipes(request):
    recipes = Recipe.objects.all()
    context = {
        "title": "Рецепты",
        "recipes": recipes
    }
    return render(request, "Recipe/all_recipes.html", context=context)

def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = Ingredient.objects.all().filter(recipe_id=recipe_id)
    context = {
        "title": recipe.name,
        "description": recipe.description,
        "ingredients": ingredients,
        "steps": recipe.steps
    }
    return render(request, "Recipe/recipe.html", context=context)

def my_recipe(request):
    my_recipe = Recipe.objects.all().filter(user=request.user)
    context = {
        "title": "Рецепты",
        "recipes": my_recipe
    }
    return render(request, "Recipe/my_recipes.html", context=context)