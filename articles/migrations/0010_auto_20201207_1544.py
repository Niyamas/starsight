# Generated by Django 3.1.4 on 2020-12-07 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20201207_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articledetailpage',
            old_name='title_subtext',
            new_name='banner_text',
        ),
    ]