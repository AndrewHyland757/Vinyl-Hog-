# Generated by Django 5.0.6 on 2024-07-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_recommendationpost_created_on'),
        ('products', '0002_remove_album_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendationpost',
            name='product',
        ),
        migrations.AddField(
            model_name='recommendationpost',
            name='product',
            field=models.ManyToManyField(to='products.album'),
        ),
    ]
