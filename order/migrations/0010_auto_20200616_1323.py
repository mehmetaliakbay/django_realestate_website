# Generated by Django 3.0.4 on 2020-06-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20200616_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproperty',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('New', 'New'), ('Canceled', 'Canceled')], default='New', max_length=10),
        ),
    ]
