from django import template

from ..models import Category


register = template.Library()


@register.inclusion_tag('app/sidebar.html')
def sidebar(current_category=None):
    return {
        'categories': Category.objects.all(),
        'current_category': current_category
    }
