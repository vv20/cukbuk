# Generated by Django 3.2.13 on 2022-06-20 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cukbuk_app', '0005_alter_recipe_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
    ]