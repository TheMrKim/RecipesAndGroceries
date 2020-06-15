from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
#from django.template import loader

from .models import Recipe, Ingredient, Unit, RecipeIngredient


def index(request):
	recipes_list= Recipe.objects.all()[:5]
	context = {'recipes_list':recipes_list}
	return render(request, 'RecipesManagement/index.html', context) 

def new_recipe(request):
	return render(request, 'RecipesManagement/new_recipe.html')

def create_recipe(request):
	recipe = Recipe(recipe_name=request.POST['recipe_name'], pub_date=timezone.now())
	recipe.save()
	return HttpResponseRedirect(reverse('RecipesManagement:index'))

def recipe_detail(request, recipe_id):
	recipe = get_object_or_404(Recipe, pk=recipe_id)
	return render(request, 'RecipesManagement/detail.html', {'recipe': recipe, 'ingredient_list': Ingredient.objects})

def link_recipe_ingredient(request, recipe_id):
	recipe = get_object_or_404(Recipe, pk=recipe_id)
	try:
		selected_ingredient = Ingredient.objects.get(pk=request.POST['ingredient_to_link_id'])
	except (KeyError, Ingredient.DoesNotExist):
		return render(request, 'index')
	else:
		recipe_ingredient = RecipeIngredient(recipe=recipe, ingredient=selected_ingredient)
		recipe_ingredient.save()

	return HttpResponseRedirect(reverse('RecipesManagement:detail',args=(recipe.id,)))