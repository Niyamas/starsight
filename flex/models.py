"""Flexible page"""

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from streams import blocks

# Create your models here.

class FlexPage(Page):
    """Flexible page class."""

    template = 'flex/flex_page.html'

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichTextBlock()),
            ('simple_richtext', blocks.SimpleRichTextBlock()),
            ('cards', blocks.CardBlock()),
            ('cta', blocks.CTABlock()),
            ('button', blocks.ButtonBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'

    #def get_sitemap_urls(self, request):
        """Remove /resources/ and other flex pages from sitemap"""
    #    return []