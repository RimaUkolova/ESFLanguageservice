# Generated by Django 2.2.2 on 2019-06-29 04:51

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190629_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerypagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_page_carousel_item', to='home.GalleryPage', verbose_name='Галерея карусель'),
        ),
    ]
