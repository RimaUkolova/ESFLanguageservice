from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, PageChooserPanel
)
from wagtail.core.fields import RichTextField
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class ContactFields(models.Model):
    name_organization = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    telephone_2 = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    email_2 = models.EmailField(blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    post_code = models.CharField(max_length=10, blank=True)

    panels = [
        FieldPanel('name_organization',
                   'The full/formatted name of the person or organisation'),
        FieldPanel('telephone'),
        FieldPanel('telephone_2'),
        FieldPanel('email'),
        FieldPanel('email_2'),
        FieldPanel('address_1'),
        FieldPanel('address_2'),
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('post_code'),
    ]

    class Meta:
        abstract = True


# Carousel items

class CarouselItem(LinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = RichTextField(blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


# Related links

class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class TreyCarouselItem(models.Model):
    image1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', verbose_name="Изображение 1"
    )
    name1 = models.CharField(max_length=255, blank=True, verbose_name="ФИО 1")
    job1 = models.CharField(max_length=255, blank=True, verbose_name="Должность 1")
    image2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', verbose_name="Изображение 2"
    )
    name2 = models.CharField(max_length=255, blank=True, verbose_name="ФИО 2")
    job2 = models.CharField(max_length=255, blank=True, verbose_name="Должность 2")
    image3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', verbose_name="Изображение 3"
    )
    name3 = models.CharField(max_length=255, blank=True, verbose_name="ФИО 3")
    job3 = models.CharField(max_length=255, blank=True, verbose_name="Должность 3")
    panels = [
        ImageChooserPanel('image1'),
        FieldPanel('name1'),
        FieldPanel('job1'),
        ImageChooserPanel('image2'),
        FieldPanel('name2'),
        FieldPanel('job2'),
        ImageChooserPanel('image3'),
        FieldPanel('name3'),
        FieldPanel('job3'),
    ]

    class Meta:
        abstract = True


class PairCarouselItem(models.Model):
    image1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', verbose_name="Изображение 1"
    )

    image2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+', verbose_name="Изображение 2"
    )

    panels = [
        ImageChooserPanel('image1'),
        ImageChooserPanel('image2'),
    ]

    class Meta:
        abstract = True