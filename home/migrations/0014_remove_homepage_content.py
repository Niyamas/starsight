# Generated by Django 3.1.4 on 2020-12-06 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_delete_starsightsettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='content',
        ),
    ]
