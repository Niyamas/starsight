from django import template
import random

register = template.Library()

@register.simple_tag
def random_1_2_3():
    return random.randint(1, 3)