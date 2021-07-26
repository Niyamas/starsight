from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel
)
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey

# Create your models here.

class StoreListingPage(Page):
    """Lists store items."""

    template = 'store/store_listing_page.html'
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['store.StoreItemPage', 'store.StoreApparelPage']

    custom_title = models.CharField(max_length=100, blank=True, null=True, help_text='Overwrites the default title')

    content_panels = Page.content_panels + [
        FieldPanel('custom_title')
    ]

class StoreItemPage(Page):
    """Store item detail pages."""

    template = 'store/store_item_page.html'

    #name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey('store.StoreCategory', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=False, on_delete=models.SET_NULL, related_name='+')
    description = RichTextField(features=['bold', 'italic'], max_length=200, null=True, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    available = models.BooleanField(default=True, null=True, blank=True)

    content_panels = Page.content_panels + [
        #FieldPanel('name'),
        SnippetChooserPanel('category'),
        ImageChooserPanel('image'),
        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('available')
    ]

class StoreApparelPage(StoreItemPage):
    """
    Apparel item page that inherits
    from StoreItemPage.
    """

    template = 'store/store_apparel_page.html'

    # Connect store colors and sizes here

    content_panels = Page.content_panels + [
        #FieldPanel('name'),
        SnippetChooserPanel('category'),
        ImageChooserPanel('image'),

        MultiFieldPanel(
            [
                InlinePanel('store_apparel_sizes', label='Apparel Size'),
                InlinePanel('store_apparel_colors', label='Apparel Color')
            ],
            heading='Apparel Options'
        ),

        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('available')
    ]



@register_snippet
class StoreCategory(models.Model):
    """Store categories (snippets)."""

    name = models.CharField(max_length=100)

    panels = [
        FieldPanel('name')
    ]

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name







class StoreApparelSizeOrderable(Orderable):
    """
    This allows one to select one or more sizes from the Snippets
    page, which can be used in the StoreApparelPage.
    """

    page = ParentalKey('store.StoreApparelPage', related_name='store_apparel_sizes')
    size = models.ForeignKey('store.StoreApparelSize', on_delete=models.CASCADE)        # When StoreApparelSize is removed, delete all selected sizes

    panels = [
        SnippetChooserPanel('size')
    ]

class StoreApparelColorOrderable(Orderable):
    """
    This allows one to select one or more colors from the Snippets
    page, which can be used in the StoreApparelPage.
    """

    page = ParentalKey('store.StoreApparelPage', related_name='store_apparel_colors')
    color = models.ForeignKey('store.StoreApparelColor', on_delete=models.CASCADE)        # When StoreApparelSize is removed, delete all selected sizes

    panels = [
        SnippetChooserPanel('color')
    ]

@register_snippet
class StoreApparelSize(models.Model):
    """Store apparel sizes (snippets)."""

    size = models.CharField(max_length=70)

    panels = [
        FieldPanel('size')
    ]

    class Meta:
        # Change ordering to XS, S, M, L, XL
        ordering = ['size']

    def __str__(self):
        return self.size

@register_snippet
class StoreApparelColor(models.Model):
    """Store apparel colors (snippets)."""

    color = models.CharField(max_length=70)

    panels = [
        FieldPanel('color')
    ]

    class Meta:
        ordering = ['color']

    def __str__(self):
        return self.color