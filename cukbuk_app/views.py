import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Recipe
from .forms import RecipeForm
from taggit.models import Tag

@login_required
def index(request):
    tags = Tag.objects.all()
    context = {
            'tags': tags
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

@login_required
def recipes(request):
    query_tags = request.GET.get('tags', '')
    if len(query_tags) == 0:
        return __all_recipes(request)
    else:
        return __recipes_with_tags(request, query_tags.split(','))

def __recipes_with_tags(request, query_tags):
    recipes = Recipe.objects.all()
    recipe_scores = []
    for recipe in recipes:
        recipe_tags = recipe.tags.names()
        score = len([t for t in recipe_tags if t in query_tags])
        if score > 0:
            recipe_scores.append((recipe, score))
    template = loader.get_template('recipes.html')
    recipe_scores.sort(key=lambda rs:rs[1], reverse=True)
    context = {
            'recipes': [r[0] for r in recipe_scores]
    }
    return HttpResponse(template.render(context, request))

def __all_recipes(request):
    recipes = Recipe.objects.all()
    template = loader.get_template('recipes.html')
    context = {
            'recipes' : recipes
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
