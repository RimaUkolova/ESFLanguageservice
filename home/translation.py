from .models import (HomePage, AboutPage, PricePage, SpecialistsPage, ContactPage, TestimonialsPage, 
    CarouselItem, GalleryPage,
    # GalleryPageCarouselItem,
    )
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'text',
    )



@register(AboutPage)
class HomePageTR(TranslationOptions):
    fields = (
        'page_slogan',
        'text1',
        'text2',
        'text3',
    )

@register(PricePage)
class PricePageTR(TranslationOptions):
	pass

@register(SpecialistsPage)
class SpecialistPageTR(TranslationOptions):
	fields = (
		'page_slogan',
	)

@register(ContactPage)
class ContactPageTR(TranslationOptions):
    fields = (
        
        'address',
        'how',
    )


@register(TestimonialsPage)
class TestimonialsPageTR(TranslationOptions):
    fields = (
        'intro',
    )

# @register(CarouselItem)
# class TestimonialsPageTR(TranslationOptions):
#     pass

@register(GalleryPage)
class GalleryPageTR(TranslationOptions):
    pass

