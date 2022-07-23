from django import forms
from .models import Recipe
from djrichtextfield.widgets import RichTextWidget
from pyquery import PyQuery

class RecipeForm(forms.ModelForm):
    image_container = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'tags')
        widgets = {
                'description': RichTextWidget()
        }

    def save(self, commit=True):
        instance = super(RecipeForm, self).save(commit=False)
        pq = PyQuery(self.cleaned_data['description'])
        images = pq('img')
        print(instance)
        if len(images) > 0:
            instance.image = images[0].attrib['src']
        else:
            instance.image = '/default_recipe_image.png'
        if commit:
            instance.save()
        return instance
