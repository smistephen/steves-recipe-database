# Generated by Django 2.1 on 2018-08-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipes.Ingredient'),
        ),
    ]
