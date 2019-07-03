from django import template
from services.models import ServicesCategoryPage
from home.models import TestimonialItem


register = template.Library()


@register.inclusion_tag('tags/all-sevices.html', takes_context=True)
def all_services(context):
    category = ServicesCategoryPage.objects.filter(live=True, show_in_menus=True)
    return {'category': category, }


@register.inclusion_tag('tags/testymonial-showcase.html', takes_context=True)
def testy_show(context):
    items = TestimonialItem.objects.all()
    return {'items': items, }


@register.inclusion_tag('tags/testimonial.html', takes_context=True)
def testy(context):
    items = TestimonialItem.objects.all()
    return {'items': items, }


