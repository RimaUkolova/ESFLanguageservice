# Generated by Django 2.2.2 on 2019-06-30 15:10

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_testimonialitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceitem',
            name='price',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Прайс'),
        ),
    ]
