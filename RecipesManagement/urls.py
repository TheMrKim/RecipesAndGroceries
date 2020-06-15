from django.urls import path
from . import views

app_name = 'RecipesManagement'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('<int:recipe_id>/', views.recipe_detail, name ='detail'),
    path('<int:recipe_id>/lol/', views.link_recipe_ingredient, name ='link_recipe_ingredient'),
]