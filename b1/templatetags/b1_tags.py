from django import template
from b1.models import *
from django.db.models import Count

register = template.Library()

@register.simple_tag(name='get_cats')      # превращаем функцию в тег при помози декоратора
def get_categories():
    cats = Category.objects.annotate(Count('women'))
    return cats
