# -*- coding: utf-8 -*-
from django import forms
# from captcha.fields import CaptchaField

#_______________________________________БЫЛО_________________
# from modelcluster.fields import ParentalKey




from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)

from modelcluster.fields import ParentalKey

from wagtail.core.fields import RichTextField
from wagtailcaptcha.models import WagtailCaptchaEmailForm


# class FeedBackForm1(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control required", "id": "fname1",
#                            "placeholder": "Il vostro nome *"}), max_length=150, required=True)
#     phone = forms.CharField(max_length=100, required= True,
#                             widget=forms.TextInput(attrs={"id": "fphone1", "class": "form-control required phone",
#                             "placeholder": "Telefono *"}))
#     captcha = CaptchaField(id_prefix="captcha2")


# class FeedBackForm2(forms.Form):
#     # TIME_LIST = (
#     #     ('09:00', '09:00'),
#     #     ('09:30', '09:30'),
#     #     ('10:00', '10:00'),
#     #     ('10:30', '10:30'),
#     #     ('11:00', '11:00'),
#     #     ('11:30', '11:30'),
#     #     ('12:00', '12:00'),
#     #     ('12:30', '12:30'),
#     #     ('13:00', '13:00'),
#     #     ('13:30', '13:30'),
#     #     ('14:00', '14:00'),
#     #     ('14:30', '14:30'),
#     #     ('15:00', '15:00'),
#     #     ('15:30', '15:30'),
#     #     ('16:00', '16:00'),
#     #     ('16:30', '16:30'),
#     #     ('17:00', '17:00'),
#     #     ('17:30', '17:30'),
#     #     ('18:00', '18:00'),
#     #     ('18:30', '18:30'),
#     #     ('19:00', '19:00'),
#     #     ('19:30', '19:30'),
#     #         )
#     name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control required", "id": "fname2",
#                            "placeholder": "Il vostro nome *"}), max_length=150, required=True)
#     phone = forms.CharField(max_length=100, required= True,
#                             widget=forms.TextInput(attrs={"id": "fphone2", "class": "form-control required phone",
#                             "placeholder": "Telefono *"}))
#     email = forms.CharField(max_length=100, required= True,
#                             widget=forms.TextInput(attrs={"id": "femail2", "class": "form-control required email",
#                             "placeholder": "Email *"}))
#     need_product = forms.CharField(max_length=300,
#                             widget=forms.Textarea(attrs={"id": "need_product2", "class": "form-control",
#                             "placeholder": "Servize "}))
#     captcha = CaptchaField(id_prefix="captcha3")  
#     # time = forms.CharField(widget=forms.Select(attrs={"class": "form-control", "aria-invalid": "false", "id": "ftime2",
#     #                                                   "placeholder": "Tempo"}, choices=TIME_LIST),required=True)
#     # date = forms.CharField(widget=forms.DateInput(attrs={"class": "form-control datetime required",
#     #                       "id": "datepicker2",
#     #                       "placeholder": "Data"}),
#     #                       required=True)


# class FeedBackForm3(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control required", "id": "fname3",
#                            "placeholder": "Il vostro nome *"}), max_length=150, required=True)
#     phone = forms.CharField(max_length=100, required= True,
#                             widget=forms.TextInput(attrs={"id": "fphone3", "class": "form-control required phone",
#                             "placeholder": "Telefono *"}))
#     need_product = forms.CharField(max_length=300,
#                             widget=forms.Textarea(attrs={"id": "need_product3", "class": "form-control",
#                             "placeholder": "Messago "}))
#     file = forms.FileField()
#     captcha = CaptchaField(id_prefix="c3")



class FeedBackForm_1_Field(AbstractFormField):
    page = ParentalKey('FeedBackForm_1_Page', related_name='FBForm_1')

class FeedBackForm_1_Page(WagtailCaptchaEmailForm):
    name = RichTextField(blank=True, help_text='Имя')
    phone = RichTextField(blank=True, help_text='Номер телефона')
    need_product = RichTextField(blank=True, help_text='продукт')

    class Meta:
        verbose_name = "Отзыв 1"

FeedBackForm_1_Page.content_panels = [
    FieldPanel('title', classname = 'full title'),
    FieldPanel('name', classname = 'full'),
    FieldPanel('phone', classname = 'full'),
    FieldPanel('need_product', classname = 'full'),
    InlinePanel('FBForm_1', label = 'Form Fields 1'),
    MultiFieldPanel([
        FieldPanel('to_address'),
        FieldPanel('from_address'),
        FieldPanel('subject'),
    ], "Email notification")    
]

class FeedBackForm_2_Field(AbstractFormField):
    page = ParentalKey('FeedBackForm_2_Page', related_name='FBForm_2')

class FeedBackForm_2_Page(WagtailCaptchaEmailForm):
    name = RichTextField(blank=True, help_text='Имя')
    phone = RichTextField(blank=True, help_text='Номер телефона')
    need_product = RichTextField(blank=True, help_text='продукт')

    class Meta:
        verbose_name = "Отзыв 2"

FeedBackForm_2_Page.content_panels = [

    FieldPanel('title', classname = 'full title'),
    FieldPanel('name', classname = 'full'),
    FieldPanel('phone', classname = 'full'),
    FieldPanel('need_product', classname = 'full'),
    InlinePanel('FBForm_2', label = 'Form Fields 1'),
    MultiFieldPanel([
        FieldPanel('to_address'),
        FieldPanel('from_address'),
        FieldPanel('subject'),
    ], "Email notification")    
]

class FeedBackForm_3_Field(AbstractFormField):
    page = ParentalKey('FeedBackForm_1_Page', related_name='FBForm_3')

class FeedBackForm_3_Page(WagtailCaptchaEmailForm):
    name = RichTextField(blank=True, help_text='Имя')
    phone = RichTextField(blank=True, help_text='Номер телефона')
    need_product = RichTextField(blank=True, help_text='продукт')

    class Meta:
        verbose_name = "Отзыв 3"

FeedBackForm_3_Page.content_panels = [

    FieldPanel('title', classname = 'full title'),
    FieldPanel('name', classname = 'full'),
    FieldPanel('phone', classname = 'full'),
    FieldPanel('need_product', classname = 'full'),
    InlinePanel('FBForm_3', label = 'Form Fields 1'),    
    MultiFieldPanel([
        FieldPanel('to_address'),
        FieldPanel('from_address'),
        FieldPanel('subject'),
    ], "Email notification")    
]