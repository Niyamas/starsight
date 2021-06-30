"""Menus models."""

from django.db import models
#from django_extensions.db.fields import AutoSlugField
from django.utils.text import slugify 

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


class NavigationItem(Orderable):
    """Individual navigation link model."""

    link_title = models.CharField(max_length=50, blank=False, null=True)
    link_url = models.CharField(max_length=500, blank=True)
    link_page = models.ForeignKey('wagtailcore.Page', blank=True, null=True, related_name='+', on_delete=models.CASCADE)
    open_in_new_tab = models.BooleanField(default=False, blank=True)
    page = ParentalKey('Navigation', related_name='navigation_items')               # Link to Menu ClusterableModel

    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        """Prioritizes link_page over link_url for linking."""

        if self.link_page:
            return self.link_page.url

        elif self.link_url:
            return self.link_url

        return '#'

    #@property
    #def title(self):
    #    """If link_title is not required, add logic to cover missing titles."""

    #    if self.link_page and not self.link_title:
    #        return self.link_page.title
    #    elif self.link_title:
    #        return self.link_title
    #    return 'Missing Title'


@register_snippet
class Navigation(ClusterableModel):
    """The main menu clusterable model."""

    title = models.CharField(max_length=100)
    #slug = AutoSlugField(populate_from='title', editable=True)          # Auto-populates the slug field after changing title

    slug = models.SlugField(unique=True, blank=False, null=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
        ], heading='Navigation'),
        InlinePanel('navigation_items', label='Navigation Item')                    # Referenced in MenuItem's page ParentalKey
    ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Navigation, self).save(*args, **kwargs)

        self.slug = slugify(self.title, allow_unicode=True)
        
        return super(Navigation, self).save(*args, **kwargs)