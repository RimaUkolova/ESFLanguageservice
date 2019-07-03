from django.db import models


from wagtail.search import index
from utils.models import LinkFields, RelatedLink, CarouselItem, PairCarouselItem, TreyCarouselItem
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
# from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.snippets.models import register_snippet

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL')
    instagram = models.CharField(
        max_length=255, help_text='Your Instagram username, without the @')
    trip_advisor = models.URLField(
        help_text='Your Trip Advisor page URL')
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL')

@register_setting
class SiteBranding(BaseSetting):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', verbose_name= "Изображение логотипа"
    )
    site_name = models.CharField(max_length=250, null=True, blank=True, verbose_name= "Название сайта")
    panels = [
        ImageChooserPanel('logo'),
        FieldPanel('site_name'),
    ]


@register_snippet
class MainNewsSnippet(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название ряда акций", default="Акции")
    link_page1 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+', verbose_name="Первая акция"
    )
    link_page2 = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+', verbose_name="Вторая акция"
    )

    panels = [
        FieldPanel('name'),
        PageChooserPanel('link_page1'),
        PageChooserPanel('link_page2'),
    ]

    class Meta:
        verbose_name_plural = "Акции на главной"

    def __str__(self):
        return self.name

class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('HomePage', related_name='carousel_items', verbose_name='Домшняя карусель')


class AboutPageCarouselItem(Orderable, TreyCarouselItem):
    page = ParentalKey('AboutPage', related_name='carousel_items_about')


class AdvantageAboutItem(Orderable):
    page = ParentalKey('AboutPage', related_name='advantage_item')
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name="Название преимущества")
    text = RichTextField( null=True, blank=True, verbose_name="Текст преимущества")

    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
    ]

class GalleryAboutItem(Orderable):
    page = ParentalKey('AboutPage', related_name='gallery_item')
    image = models.ForeignKey(
        'wagtailimages.Image',
        help_text="Изображение для галлереи",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        ImageChooserPanel('image'),
    ]

class LicenseAboutItem(Orderable):
    page = ParentalKey('AboutPage', related_name='license_item')
    image = models.ForeignKey(
        Image,
        help_text="Лицензии страницы 'about'",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        ImageChooserPanel('image'),
    ]


class HomePage(Page):
    page_slogan = models.CharField(max_length=250, null=True, blank=True, verbose_name="Лозунг страницы")
    # text = RichTextField(editor='tinymce', null=True, blank=True, verbose_name="Текст")
    text = RichTextField(null=True, blank=True, verbose_name="Текст")
    # editor='tinymce',
    hidden_text = RichTextField(null=True, blank=True, verbose_name="Скрытый текст")
    feed_image = models.ForeignKey(
        Image,
        help_text="An optional image to represent the page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )

    search_fields = Page.search_fields + [
        index.SearchField('text'),

    ]

    content_panels = Page.content_panels + [
        FieldPanel('page_slogan'),
        FieldPanel('text'),
        FieldPanel('hidden_text'),

        InlinePanel('carousel_items'),
        # InlinePanel('carousel_items'),
        ]

    class Meta:
        verbose_name = "Главная"

#____О компании____
class AboutPage(Page):
    page_slogan = models.CharField(max_length=250, null=True, blank=True, verbose_name="Лозунг страницы")
    text1 = RichTextField( null=True, blank=True, verbose_name="Текст1")
    text2 = RichTextField( null=True, blank=True, verbose_name="Текст2")
    text3 = RichTextField( null=True, blank=True, verbose_name="Текст3")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        help_text="An optional image to represent the page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [

        FieldPanel("page_slogan"),
        FieldPanel('text1'),
        FieldPanel('text2'),
        FieldPanel('text3'),
        InlinePanel('advantage_item', label="Преимущества компании"),
        InlinePanel('carousel_items_about', label="Карусель для страницы \"О компании\" "),

    ]

    search_fields = Page.search_fields + [
        
        index.SearchField('page_slogan'),
        index.SearchField('text1'),
        index.SearchField('text2'),
        index.SearchField('text3'),
    ]

    promote_panels = [

        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),

    ]


#____Специалисты____
class SpecialistsPageCarouselItem(Orderable, TreyCarouselItem):
    page = ParentalKey('SpecialistsPage', related_name='specialists_carousel_items')

class SpecialistsPage(Page):
    page_slogan = models.CharField(max_length=250, null=True, blank=True, verbose_name="Лозунг страницы")
    text1 = RichTextField(null=True, blank=True, verbose_name="Текст1")

    search_fields = Page.search_fields + [
        index.SearchField('page_slogan'),
        # index.FilterField('date'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('text1', classname='ull'),
        FieldPanel('title', classname="full title"),
        InlinePanel('specialists_carousel_items', label="Специалисты"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        # ImageChooserPanel('feed_image'),
    ]
    class Meta:
        verbose_name_plural="Специалисты"
        verbose_name="Специалист"


#____Цены____
class PricePage(Page):
    search_fields = Page.search_fields + [
        index.SearchField('title'),
        # index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        # FieldPanel('date'),
        FieldPanel('title', classname="full title"),
        InlinePanel('priceitem_p', label="Цены"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page"),

        # ImageChooserPanel('feed_image'),
    ]

class PriceItem(Orderable):
    page = ParentalKey(PricePage, on_delete=models.CASCADE, related_name='priceitem_p')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, verbose_name="Slug категории прайса", unique=True)
    price = RichTextField(null=True, blank=True, verbose_name="Прайс")

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('price')
    ]

#____Контакты____
class ContactPage(Page):
    address = models.CharField(max_length=250, verbose_name="Адрес", blank=True, null=True)
    phone = models.CharField(max_length=250, verbose_name="Телефон", blank=True, null=True)
    email = models.EmailField(max_length=250, verbose_name="E-mail", blank=True, null=True)
    schedule = models.CharField(max_length=250, verbose_name="Расписание", blank=True, null=True)
    how = RichTextField(blank=True, null=True, verbose_name="Как добраться")
    contact_map = models.TextField(verbose_name="Карта", help_text="Разместите код карты", blank=True, null=True) 


    search_fields = Page.search_fields + [
        index.SearchField('title'),
        # index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        # FieldPanel('date'),
        FieldPanel('title', classname="full title"),
        FieldPanel('address', classname="full"),
        FieldPanel('phone', classname="full"),
        FieldPanel('email', classname="full"),
        FieldPanel('schedule', classname="full"),
        FieldPanel('how', classname="full"),
        FieldPanel('contact_map', classname="full"),       
        # InlinePanel('priceitem_p', label="Прайс цен"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),

    ]




class TestimonialsPage(Page):
    # page_slogan = models.CharField(max_length=250, null=True, blank=True, verbose_name="Лозунг страницы")
    intro = RichTextField(null=True, blank=True, verbose_name="Текст1")

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        # index.FilterField('date'),
    ]
    content_panels = Page.content_panels + [
        # ImageChooserPanel('testimonial_item'),
        FieldPanel('intro', classname='ull'),
        # FieldPanel('title', classname="full title"),
        InlinePanel('testimonial_item', label="Отзыв"),

    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Testinonial page"),
        # ImageChooserPanel('feed_image'),
    ]

    def get_context(self, request):
        context = super(TestimonialsPage, self).get_context(request)
        all_testimonuials = TestimonialsPage.objects.all()
        page = request.GET.get('page')
        paginator = Paginator(all_testimonuials, 6)
        try:
            testimonial=paginator.page(page)
        except PageNotAnInteger:
            testimonial = paginator.page(1)
        except EmptyPage:
            testimonial = paginator.page(paginator.num_pages)
        context['testimonial'] = testimonial
        return context




class TestimonialItem(Orderable):
    page = ParentalKey(TestimonialsPage, on_delete=models.CASCADE, related_name='testimonial_item')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', verbose_name= "Изображение"
    )    
    name = models.CharField(max_length=255, verbose_name='имя')
    job = models.CharField(max_length=255, verbose_name='должность', blank=True, null=True)

    slug = models.SlugField(max_length=250, verbose_name="Slug категории прайса", unique=True)
    text = RichTextField( null=True, blank=True, verbose_name="Текст")

    panels = [
        FieldPanel('name', classname="full title"),
        FieldPanel('job', classname="full"),
        FieldPanel('text', classname="full"),
        ImageChooserPanel('image'),
    ]
    class Meta:
        verbose_name="Отзыв"
        verbose_name_plural="Отзывы"



#____Галлерея____
class GalleryPage(Page):
    # page_slogan = models.CharField(max_length=250, null=True, blank=True, verbose_name="Лозунг страницы")
    intro = RichTextField(null=True, blank=True, verbose_name="Текст1")


    content_panels = Page.content_panels + [

        InlinePanel('gallery_page_carousel_item', label="карусель"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Gallery page"),
        # ImageChooserPanel('feed_image'),
    ]

class GalleryPageCarouselItem(Orderable, PairCarouselItem):
    page = ParentalKey(GalleryPage, related_name='gallery_page_carousel_item', verbose_name='Галерея карусель')