# Generated by Django 3.0.4 on 2020-03-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20200321_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='images/'),
        ),
    ]