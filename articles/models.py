"""Article listing and detail pages."""

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

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

    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text='Overwrites the default title')
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
        FieldPanel('custom_title'),
        ImageChooserPanel('image'),
        StreamFieldPanel('content')

    ]