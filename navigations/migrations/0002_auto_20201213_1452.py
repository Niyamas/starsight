# Generated by Django 3.1.4 on 2020-12-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationitem',
            name='link_title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]