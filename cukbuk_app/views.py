import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Recipe
from .forms import RecipeForm

@login_required
def index(request):
    recipes = Recipe.objects.all()
    template = loader.get_template('index.html')
    context = {
            'recipes': recipes
    }
    return HttpResponse(template.render(context, request))

@login_required
def edit(request, slug):
    return {
            'GET': __edit_get,
            'POST': __edit_post,
            'DELETE': __edit_delete,
    }.get(request.method)(request, slug)

def __edit_get(request, slug):
        if slug == 'new':
            form = RecipeForm()
        else:
            recipe = Recipe.objects.get(slug=slug)
            form = RecipeForm(instance=recipe)
        template = loader.get_template('edit.html')
        return HttpResponse(template.render({'form': form}, request))

def __edit_post(request, slug):
    if Recipe.objects.filter(slug=slug):
        recipe = Recipe.objects.get(slug=slug)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
    else:
        form = RecipeForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('index'))

def __edit_delete(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    recipe.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required
def recipe(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    template = loader.get_template('recipe.html')
    context = {
            'recipe': recipe
    }
    return HttpResponse(template.render(context, request))

@login_required
def randomrecipe(request):
    recipes = list(Recipe.objects.all())
    recipe = random.choice(recipes)
    return HttpResponseRedirect(recipe.get_absolute_url())
