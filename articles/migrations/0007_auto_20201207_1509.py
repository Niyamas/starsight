# Generated by Django 3.1.4 on 2020-12-07 21:09

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20201207_1504'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleCategory',
            new_name='ArticleTopic',
        ),
        migrations.AddField(
            model_name='articledetailpage',
            name='topics',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='articles.ArticleTopic'),
        ),
    ]
