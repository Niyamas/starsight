"""Article listing and detail pages."""

from django.db import models
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django_extensions.db.fields import AutoSlugField
#from django import forms
#from django.shortcuts import render

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel
)
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from modelcluster.fields import (
    ParentalKey,
    #ParentalManyToManyField
)
#from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from streams import blocks

# Create your models here.

class ArticleListingPage(Page):
    """Lists all the blog pages."""

    template = 'articles/article_listing_page.html'

    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text='Overwrites the default title')

    content_panels = Page.content_panels + [
        FieldPanel('custom_title')
    ]

    def get_context(self, request, *args, **kwargs):
        """Add additional context."""
        context = super().get_context(request, *args, **kwargs)
        #context['articles'] = ArticleDetailPage.objects.live().public().order_by('-first_published_at')

        # Query all articles for paginator
        articles = ArticleDetailPage.objects.live().public().order_by('-first_published_at')

        # Filter articles by the topic selected by the user
        # Has an issue with pagination
        topic_slug = request.GET.get('topic', None)
        if topic_slug:
            articles = articles.filter(topic__slug=topic_slug)

        # Create paginator and paginate by 2
        paginator = Paginator(articles, 2)
        page = request.GET.get('page')

        try:
            articles_paginated = paginator.page(page)                     # Get the page if it exists
        except PageNotAnInteger:
            articles_paginated = paginator.page(1)                        # Return first page if page isn't an integer
        except EmptyPage:
            articles_paginated = paginator.page(paginator.num_pages)      # Return last page if user goes out of paginator range

        context['articles'] = articles_paginated

        context['topics'] = ArticleTopic.objects.all()

        # For passing the topic slug when the user selects a topic
        context['topic_pagination'] = topic_slug

        print(context['topic_pagination'])

        return context

class ArticleDetailPage(Page):
    """Article detail page."""

    template = 'articles/article_detail_page.html'

    banner_text = RichTextField(features=['bold', 'italic'], max_length=200, null=True, blank=False)
    topic = models.ForeignKey('articles.ArticleTopic', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    image_credits = models.CharField(max_length=100, blank=False, null=True, help_text="Acknowledge the image's producer")
    content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichTextBlock()),
            ('simple_richtext', blocks.SimpleRichTextBlock()),
            ('cards', blocks.CardBlock()),
            ('cta', blocks.CTABlock()),
        ],
        null=True,
        blank=True
    )
    date = models.DateTimeField(default=timezone.now)

    content_panels = Page.content_panels + [
        FieldPanel('banner_text'),
        SnippetChooserPanel('topic'),
        MultiFieldPanel(
            [
                ImageChooserPanel('image'),
                FieldPanel('image_credits')
            ],
            heading='Header Image'
        ),
        MultiFieldPanel(
            [
                InlinePanel('article_authors', label='Author', min_num=1, max_num=3)
            ],
            heading='Author(s)'
        ),
        StreamFieldPanel('content'),
        FieldPanel('date')
    ]



class VideoArticlePage(ArticleDetailPage):
    """
    Video article page that inherits from
    ArticleDetailPage
    """

    template = 'articles/video_article_page.html'

    youtube_video_id = models.CharField(max_length=30)

    content_panels = Page.content_panels + [
        FieldPanel('banner_text'),
        ImageChooserPanel('image'),
        #FieldPanel('topic'),
        SnippetChooserPanel('topic'),
        MultiFieldPanel(
            [
                InlinePanel('article_authors', label='Author', min_num=1, max_num=3)
            ],
            heading='Author(s)'
        ),
        FieldPanel('youtube_video_id'),
        StreamFieldPanel('content'),
        FieldPanel('date')
    ]


class ArticleDetailPageStrange(ArticleDetailPage):
    """Inherits from ArticleDetailPage"""

    template = 'articles/article_detail_page_strange.html'

    strange_quote = models.CharField(max_length=100, null=True, blank=True, help_text='Add a strange quote you know!')

    content_panels = Page.content_panels + [
        FieldPanel('banner_text'),
        FieldPanel('strange_quote'),
        ImageChooserPanel('image'),
        #FieldPanel('topic'),
        SnippetChooserPanel('topic'),
        MultiFieldPanel(
            [
                InlinePanel('article_authors', label='Author', min_num=1, max_num=3)
            ],
            heading='Author(s)'
        ),
        StreamFieldPanel('content'),
        FieldPanel('date')
    ]











class ArticleAuthorsOrderable(Orderable):
    """
    This allows us to select one or more authors from the Snippets page,
    which can be used in the article detail pages
    """

    page = ParentalKey('articles.ArticleDetailPage', related_name='article_authors')
    author = models.ForeignKey(
        'articles.ArticleAuthor',
        on_delete=models.CASCADE,           # When ArticleAuthor instance is removed, remove all selected authors.
    )

    panels = [
        SnippetChooserPanel('author')
    ]


@register_snippet
class ArticleAuthor(models.Model):
    """
    Article author for snippets using
    vanilla Django models.
    """

    name = models.CharField(max_length=100)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    website = models.URLField(blank=True, null=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('name'),
                ImageChooserPanel('image')
            ],
            heading='Author Information'
        ),
        MultiFieldPanel(
            [
                FieldPanel('website'),
            ],
            heading='Author Links'
        )
    ]

    class Meta:
        verbose_name = 'Article Author'
        verbose_name_plural = 'Article Authors'
        #ordering = ['name']

    def __str__(self):
        """
        For vanilla Django to know how to name each model
        object created.
        """
        return self.name

#register_snippet(ArticleAuthor)

@register_snippet
class ArticleTopic(models.Model):
    """
    Article topics that resides in Snippets.
    """

    name = models.CharField(max_length=100)
    #slug = models.SlugField(
    #    max_length=150,
    #    verbose_name='slug',
    #    allow_unicode=True,
    #    help_text='A slug to identify articles by this topic.'
    #)

    slug = AutoSlugField(
        populate_from='name',
        editable=True,
        max_length=100,
        verbose_name='slug',
        allow_unicode=True,
        help_text='A slug to identify articles by this topic.'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug')
    ]

    class Meta:
        verbose_name = 'Article Topic'
        verbose_name_plural = 'Article Topics'
        ordering = ['name']                             # Alphabetial ordering

    def __str__(self):
        return self.name

#register_snippet(ArticleTopic)