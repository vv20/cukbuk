from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
#    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
