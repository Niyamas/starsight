# Generated by Django 3.1.4 on 2021-01-19 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_storelistingpage_custom_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeitempage',
            name='name',
        ),
    ]