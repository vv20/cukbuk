from django import forms
from image_uploader_widget.widgets import ImageUploaderWidget
from .models import Recipe

class RecipeForm(forms.ModelForm):
    image_container = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'image')
        '''
        widgets = {
                'image': ImageUploaderWidget()
        }
        '''
