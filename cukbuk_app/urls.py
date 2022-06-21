from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<slug:slug>', views.edit, name='edit'),
    path('recipe/<slug:slug>', views.recipe, name='recipe'),
    path('randomrecipe/', views.randomrecipe, name='randomrecipe')
]
