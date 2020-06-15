from django import forms

class RecipeForm(forms.Form):
	recipe_name = forms.CharField(label='Recipe name', max_length=100)