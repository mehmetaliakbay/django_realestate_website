# Generated by Django 3.0.4 on 2020-04-10 10:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20200402_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
