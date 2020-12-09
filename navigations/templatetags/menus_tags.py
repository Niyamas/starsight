"""
Enables the {% load menus_tags %} in base.html. Provides the navigation menu
item slugs as an alternative to using a context processor.
"""

from django import template
from ..models import Navigation

register = template.Library()

@register.simple_tag()
def get_navigation(slug):
    return Navigation.objects.get(slug=slug)