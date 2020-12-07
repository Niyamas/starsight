"""Article listing and detail pages."""

from django.db import models
from django.utils import timezone
#from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
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
        context['articles'] = ArticleDetailPage.objects.live().public()
        return context

class ArticleDetailPage(Page):
    """Article detail page."""

    title_subtext = RichTextField(features=['bold', 'italic'], max_length=200, null=True, blank=False)
    date = models.DateTimeField(default=timezone.now)

    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
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

    content_panels = Page.content_panels + [
        FieldPanel('title_subtext'),
        ImageChooserPanel('image'),
        StreamFieldPanel('content'),
        FieldPanel('date')

    ]



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

    def __str__(self):
        """
        For vanilla Django to know how to name each model
        object created.
        """
        return self.name

register_snippet(ArticleAuthor)