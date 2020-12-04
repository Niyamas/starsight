from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

from streams import blocks

from decouple import config


class HomePage(Page):
    """Home page model"""

    templates = 'home/home_page.html'
    max_count = 1                       # Max number of home pages will be 1

    default_apod_image = models.ForeignKey('wagtailimages.Image', null=True, blank=False, on_delete=models.SET_NULL, related_name='+')
    default_apod_image_title = models.CharField(max_length=100, null=True, blank=False)
    default_apod_image_credits = models.CharField(max_length=100, null=True, blank=False)
    default_apod_image_text = RichTextField(features=['bold', 'italic'], max_length=276, null=True, blank=False)
    default_apod_image_url = models.URLField(null=True, blank=True)

    # Borrowed from streams/models.py
    content = StreamField(
        [
            ('cta', blocks.CTABlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel('default_apod_image'),
                FieldPanel('default_apod_image_title'),
                FieldPanel('default_apod_image_credits'),
                FieldPanel('default_apod_image_text'),
                FieldPanel('default_apod_image_url'),
            ],
            heading='Default Apod Image',
            classname='collapsible collapsed'
        ),
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