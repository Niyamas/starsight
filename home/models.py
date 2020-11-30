from django.db import models

from wagtail.core.models import Page

from decouple import config


class HomePage(Page):
    """Home page model"""

    templates = 'home/home_page.html'

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['nasa_api_key'] = config('NASA_API_KEY')
        return context