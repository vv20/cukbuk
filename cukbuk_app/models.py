from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.safestring import mark_safe
from djrichtextfield.models import RichTextField
from taggit.managers import TaggableManager

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    image = models.CharField(max_length=255, default='/default_recipe_image.png')
    slug = models.SlugField(null=False, unique=True)
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'slug': self.slug})

    def safe_description(self):
        return mark_safe(self.description)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
