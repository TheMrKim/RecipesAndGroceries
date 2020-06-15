#exec(open('import_db.py').read())

from RecipesManagement.models import Recipe, Unit, Ingredient, RecipeIngredient
from django.utils import timezone

Recipe.objects.all().delete()
Unit.objects.all().delete()
Ingredient.objects.all().delete()
RecipeIngredient.objects.all().delete()

r = Recipe(recipe_name="crêpes", pub_date = timezone.now())
r.save()

u_g = Unit(unit_name="g")
u_g.save()
u_pce = Unit(unit_name="pce")
u_pce.save()
u_cas  = Unit(unit_name="cuillères à soupe")
u_cas.save()
u_cl = Unit(unit_name="cl")
u_cl.save()

i_f = u_g.ingredient_set.create(ingredient_name = "farine")
i_b = u_g.ingredient_set.create(ingredient_name = "beurre")
i_o = u_pce.ingredient_set.create(ingredient_name = "oeuf")
i_s = u_cas.ingredient_set.create(ingredient_name = "sucre")
i_h = u_cas.ingredient_set.create(ingredient_name = "huile")
i_l = u_cl.ingredient_set.create(ingredient_name = "lait")
i_r = u_cl.ingredient_set.create(ingredient_name = "rhum")

ri_f = r.recipeingredient_set.create(quantity = 300, ingredient = i_f)
ri_b = r.recipeingredient_set.create(quantity = 50, ingredient = i_b)
ri_o = r.recipeingredient_set.create(quantity = 3, ingredient = i_o)
ri_s = r.recipeingredient_set.create(quantity = 3, ingredient = i_s)
ri_h = r.recipeingredient_set.create(quantity = 2, ingredient = i_h)
ri_l = r.recipeingredient_set.create(quantity = 60, ingredient = i_l)
ri_r = r.recipeingredient_set.create(quantity = 5, ingredient = i_r)

print( "It is done")