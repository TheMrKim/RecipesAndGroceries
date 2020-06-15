from django.db import models

class Recipe(models.Model):
	recipe_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date created')
	def __str__(self):
		return self.recipe_name

class Unit(models.Model):
	unit_name = models.CharField(max_length=20)
	def __str__(self):
		return self.unit_name

class Ingredient(models.Model):
	ingredient_name = models.CharField(max_length=200)
	unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
	def __str__(self):
		return self.ingredient_name

class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)