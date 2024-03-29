# Generated by Django 3.2.5 on 2021-07-22 18:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import modelcluster.contrib.taggit
import modelcluster.fields
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Article Author',
                'verbose_name_plural': 'Article Authors',
            },
        ),
        migrations.CreateModel(
            name='ArticleDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_text', wagtail.core.fields.RichTextField(max_length=200, null=True)),
                ('image_credits', models.CharField(blank=True, help_text="Acknowledge the image's producer", max_length=100, null=True)),
                ('image_credits_url', models.URLField(blank=True, max_length=500, null=True)),
                ('content', wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))])), ('full_richtext', streams.blocks.RichTextBlock()), ('simple_richtext', streams.blocks.SimpleRichTextBlock()), ('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used instead of the button URL.', required=False))])))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=60, required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=40, required=True))]))], blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ArticleListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(blank=True, help_text='Overwrites the default title', max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ArticleTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Article Topic',
                'verbose_name_plural': 'Article Topics',
                'ordering': ['name'],
            },
        ),
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
        migrations.CreateModel(
            name='VideoArticlePage',
            fields=[
                ('articledetailpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articles.articledetailpage')),
                ('youtube_video_id', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('articles.articledetailpage',),
        ),
        migrations.CreateModel(
            name='ArticlePageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='articles.articledetailpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_articlepagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='articledetailpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='articles.ArticlePageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='articledetailpage',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.articletopic'),
        ),
        migrations.CreateModel(
            name='ArticleAuthorsOrderable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articleauthor')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_authors', to='articles.articledetailpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
