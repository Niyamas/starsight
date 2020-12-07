# Generated by Django 3.1.4 on 2020-12-04 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0007_homepage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='default_apod_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='default_apod_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]