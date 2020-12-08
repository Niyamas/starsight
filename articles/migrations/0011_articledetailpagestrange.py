# Generated by Django 3.1.4 on 2020-12-08 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20201207_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDetailPageStrange',
            fields=[
                ('articledetailpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articles.articledetailpage')),
                ('strange_quote', models.CharField(blank=True, help_text='Add a strange quote you know!', max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('articles.articledetailpage',),
        ),
    ]