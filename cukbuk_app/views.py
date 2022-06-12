import random

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Recipe
from .forms import RecipeForm

def index(request):
    recipes = Recipe.objects.all()
    template = loader.get_template('index.html')
    context = {
            'recipes': recipes
    }
    return HttpResponse(template.render(context, request))

def edit(request, slug):
    if (request.method == 'GET'):
        if slug == 'new':
            form = RecipeForm()
        else:
            recipe = Recipe.objects.get(slug=slug)
            form = RecipeForm(instance=recipe)
        template = loader.get_template('edit.html')
        return HttpResponse(template.render({'form': form}, request))
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))

def deleterecord(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return HttpResponseRedirect(reverse('index'))

def recipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    template = loader.get_template('recipe.html')
    context = {
            'recipe': recipe
    }
    return HttpResponse(template.render(context, request))

def randomrecipe(request):
    recipes = list(Recipe.objects.all())
    recipe = random.choice(recipes)
    return HttpResponseRedirect(recipe.get_absolute_url())
