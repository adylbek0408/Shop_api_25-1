# Generated by Django 4.2 on 2023-04-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[[1, '*'], [2, '**'], [3, '***'], [4, '****'], [5, '*****']], default=1),
        ),
    ]
