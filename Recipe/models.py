from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

user = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    description = models.TextField()
    ingredients = models.ManyToManyField(Product, through="Ingredient")
    steps = models.TextField()

    def get_absolute_url(self):
        return reverse("recipe", kwargs={"recipe_id": self.pk})

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    class Meta:
        unique_together = ("product", "recipe")

    def __str__(self):
        return f'{self.product} - {self.quantity} {self.unit}'
