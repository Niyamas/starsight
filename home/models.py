from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

from streams import blocks

from decouple import config


class HomePage(Page):
    """Home page model"""

    templates = 'home/home_page.html'
    max_count = 1                       # Max number of home pages will be 1

    # Borrowed from streams/models.py
    content = StreamField(
    [
        ('cta', blocks.CTABlock()),
    ],
    null=True,
    blank=True
)
    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['nasa_api_key'] = config('NASA_API_KEY')
        return context


@register_setting
class StarsightSettings(BaseSetting):
    """Adds options in the admin settings."""

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name = "+"
    )

    panels = [
        ImageChooserPanel('hero_image'),
    ]