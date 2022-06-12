from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<slug:slug>', views.edit, name='edit'),
    path('delete/<int:id>', views.deleterecord, name='deleterecord'),
    path('recipe/<slug:slug>', views.recipe, name='recipe'),
    path('randomrecipe/', views.randomrecipe, name='randomrecipe')
]
