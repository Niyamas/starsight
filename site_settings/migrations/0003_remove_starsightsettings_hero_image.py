# Generated by Django 3.1.4 on 2020-12-13 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_auto_20201204_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starsightsettings',
            name='hero_image',
        ),
    ]
