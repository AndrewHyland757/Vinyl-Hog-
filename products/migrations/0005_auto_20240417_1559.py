# Generated by Django 3.2.25 on 2024-04-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20240417_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='genres',
        ),
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(blank=True, to='products.Genre'),
        ),
    ]
