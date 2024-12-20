# Generated by Django 5.0.6 on 2024-06-08 12:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Condition',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('stock', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('on_sale', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.artist')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.condition')),
                ('genres', models.ManyToManyField(blank=True, to='products.genre')),
            ],
        ),
    ]
