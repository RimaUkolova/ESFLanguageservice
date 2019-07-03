from .models import (ServicesAllPage, ServicesPage,
    ServicesCategoryPage,

    )
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(ServicesAllPage)
class ServicesAllPageTR(TranslationOptions):
    fields = (
        'text',
        'headen_text',
    )

@register(ServicesPage)
class ServicesPageTR(TranslationOptions):
    fields = (
        
        'text',
        'aside',
    )

@register(ServicesCategoryPage)
class ServicesCategoryPageTR(TranslationOptions):
    fields = (
        
        'text',
        
    )