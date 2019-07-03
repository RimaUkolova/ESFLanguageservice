# Generated by Django 2.2.2 on 2019-06-29 09:35

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesallpage',
            name='headen_text_en',
            field=models.TextField(blank=True, help_text='Разместите скрытый текст', null=True, verbose_name='Скрытый текст'),
        ),
        migrations.AddField(
            model_name='servicesallpage',
            name='headen_text_it',
            field=models.TextField(blank=True, help_text='Разместите скрытый текст', null=True, verbose_name='Скрытый текст'),
        ),
        migrations.AddField(
            model_name='servicesallpage',
            name='headen_text_ru',
            field=models.TextField(blank=True, help_text='Разместите скрытый текст', null=True, verbose_name='Скрытый текст'),
        ),
        migrations.AddField(
            model_name='servicesallpage',
            name='text_en',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='servicesallpage',
            name='text_it',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='servicesallpage',
            name='text_ru',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
