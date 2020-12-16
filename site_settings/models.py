from django.db import models

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.

@register_setting
class StarsightSettings(BaseSetting):
    """Adds options in the admin settings."""

    #hero_image = models.ForeignKey(
    #    'wagtailimages.Image',
    #    null = True,
    #    blank = False,
    #    on_delete = models.SET_NULL,
    #    related_name = "+"
    #)
    facebook = models.URLField(blank=True, null=True, help_text='Facebook URL')
    twitter = models.URLField(blank=True, null=True, help_text='Twitter URL')
    instagram = models.URLField(blank=True, null=True, help_text='Instagram URL')
    youtube = models.URLField(blank=True, null=True, help_text='YouTube Channel URL')

    panels = [
        #ImageChooserPanel('hero_image'),
        MultiFieldPanel(
            [
                FieldPanel('facebook'),
                FieldPanel('twitter'),
                FieldPanel('instagram'),
                FieldPanel('youtube')
            ],
            heading='Social Media',
        )
    ]