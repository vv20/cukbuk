from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.safestring import mark_safe
from djrichtextfield.models import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    slug = models.SlugField(null=False, unique=True)
#    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'slug': self.slug})

    def safe_description(self):
        return mark_safe(self.description)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
