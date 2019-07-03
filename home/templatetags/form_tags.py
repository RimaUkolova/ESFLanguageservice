from django import template
# from home.forms import FeedBackForm1, FeedBackForm2, FeedBackForm3
from home.forms import FeedBackForm_1_Page, FeedBackForm_2_Page, FeedBackForm_3_Page

register = template.Library()


@register.inclusion_tag('tags/feedback1.html', takes_context=True)
def feedback1(context):
    form = FeedBackForm_1_Page
    return {'form': form, }


@register.inclusion_tag('tags/feedback2.html', takes_context=True)
def feedback2(context):
    form = FeedBackForm_2_Page
    return {'form': form, }


@register.inclusion_tag('tags/feedback3.html', takes_context=True)
def feedback3(context):
    form = FeedBackForm_3_Page
    return {'form': form, }


