# Generated by Django 4.1.7 on 2023-03-08 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг категории')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Название товара')),
                ('slug', models.SlugField(unique=True, verbose_name='Адрес товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b2.category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
                ('wishlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='b2.product')),
            ],
        ),
    ]
