from django.urls import path
from . import views

app_name = 'RecipesManagement'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.recipe_detail, name ='detail'),
    path('<int:recipe_id>/lol/', views.link_recipe_ingredient, name ='link_recipe_ingredient'),
]