# Generated by Django 4.1.2 on 2022-11-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderproduct_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
