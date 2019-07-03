from django.db import models


from wagtail.search import index
from utils.models import LinkFields, RelatedLink, CarouselItem
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
# from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel



class ServicesAllPage(Page):
    text = RichTextField(blank=True, null=True, verbose_name="Текст")
    headen_text = models.TextField(verbose_name="Скрытый текст", help_text="Разместите скрытый текст", blank=True, null=True) 


    search_fields = Page.search_fields + [
        index.SearchField('text'),
        # index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        # FieldPanel('date'),
        FieldPanel('text', classname="full"),
        FieldPanel('headen_text', classname="full"),

    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),

    ]


class ServicesCategoryPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('ServicesCategoryPage', related_name='services_category_page_item')

class ServicesCategoryPage(Page):
    feed_image = models.ForeignKey(
        Image,
        help_text="An optional image to represent the page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text = RichTextField(null=True, blank=True, verbose_name="Текст")
    price_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    aside = RichTextField( null=True, blank=True, verbose_name="Текст в левой колонке")

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('text'),
        DocumentChooserPanel('price_file'),
        FieldPanel('aside'),
        InlinePanel('services_category_page_item', label="Связанные ссылки"),

    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),
    ]


    class Meta:
        verbose_name = "Услуги страница категории"



class ServicePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('ServicesPage', related_name='services_page_related_link')


class ServicesPage(Page):
    feed_image = models.ForeignKey(
        Image,
        help_text="An optional image to represent the page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text = RichTextField( null=True, blank=True, verbose_name="Текст")
    price_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    aside = RichTextField(null=True, blank=True, verbose_name="Текст в левой колонке")

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('text'),
        DocumentChooserPanel('price_file'),
        FieldPanel('aside'),
        InlinePanel('services_page_related_link', label="Связанные ссылки"),

    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),
    ]

    class Meta:
        verbose_name = "Услуги одиночная страница"