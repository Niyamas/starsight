from django.db import models

from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.

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