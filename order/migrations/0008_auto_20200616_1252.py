# Generated by Django 3.0.4 on 2020-06-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200616_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproperty',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Canceled', 'Canceled'), ('New', 'New')], default='New', max_length=10),
        ),
    ]