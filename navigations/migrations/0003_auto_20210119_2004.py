# Generated by Django 3.1.5 on 2021-01-20 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigations', '0002_auto_20201213_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
