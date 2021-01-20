from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from modelcluster.fields import ParentalKey

from streams import blocks
from articles.models import (
    ArticleDetailPage,
    ArticleAuthor
)

from decouple import config


class HomePage(RoutablePageMixin, Page):
    """Home page model"""

    templates = 'home/home_page.html'
    max_count = 1                       # Max number of home pages will be 1

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name = "+"
    )

    default_apod_image = models.ForeignKey('wagtailimages.Image', null=True, blank=False, on_delete=models.SET_NULL, related_name='+')
    default_apod_image_title = models.CharField(max_length=100, null=True, blank=False)
    default_apod_image_credits = models.CharField(max_length=100, null=True, blank=False)
    default_apod_image_text = RichTextField(features=['bold', 'italic'], max_length=276, null=True, blank=False)
    default_apod_image_url = models.URLField(null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('hero_image'),
        MultiFieldPanel(
            [
                ImageChooserPanel('default_apod_image'),
                FieldPanel('default_apod_image_title'),
                FieldPanel('default_apod_image_credits'),
                FieldPanel('default_apod_image_text'),
                FieldPanel('default_apod_image_url'),
            ],
            heading='Default Apod Image',
            classname='collapsible'
        ),

        MultiFieldPanel(
            [
                InlinePanel('carousel_images', max_num=5, min_num=1, label='Image')
            ],
            heading='Carousel Images',
            classname='collapsible'
        )
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Pass the NASA API key from .env to the template
        context['nasa_api_key'] = config('NASA_API_KEY')

        # Get all live & public articles from the database and pass to the template
        context['articles'] = ArticleDetailPage.objects.live().public().order_by('-first_published_at')

        context['authors'] = ArticleAuthor.objects.all()
        
        return context

    #@route(r'^subscribe/$')
    @route('subscribe/')
    def subscribe_page(self, request, *args, **kwargs):
        """
        Adds a routable page that inherits from get_context() method and tacks on
        an additional page associated with the homepage.
        """
        context = self.get_context(request, *args, **kwargs)
        return render(request, 'home/subscribe.html', context)

    def get_sitemap_urls(self, request):
        """
        Register routable page (subscribe) to sitemap.xml.
        Return an empty list instead to remove the this page from the sitemap
        """

        return []

        #sitemap = super().get_sitemap_urls(request)

        # Add subscribe_page to the sitemap
        """ sitemap.append(
            {
                'location': self.full_url + self.reverse_subpage('subscribe_page'),
                'lastmod': (self.last_published_at or self.latest_revision_created_at),     # Not accurate--uses the home page publish date for the subscribe page
                #'priority': 0.9                                                            # Look up priority value (0-1) for SEO purposes
            }
        ) """
        #return sitemap



class HomePageCarouselImages(Orderable):
    """
    Between 1 and 5 images for the home page carousel. Similar to inline models in Django.
    Orderables differ from streamfields in that one can set a minimum or maximum number of
    objects. Another is that orderables are not restricted to the forloop template tag and
    can be placed anywhere on the html page.
    """

    page = ParentalKey('home.HomePage', related_name='carousel_images')
    carousel_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('carousel_image')
    ]