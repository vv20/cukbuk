from django import forms
from .models import Recipe
from djrichtextfield.widgets import RichTextWidget

class RecipeForm(forms.ModelForm):
    image_container = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = Recipe
        fields = ('name', 'description')
        widgets = {
                'description': RichTextWidget()
        }
