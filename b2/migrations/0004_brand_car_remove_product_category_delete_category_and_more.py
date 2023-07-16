# Generated by Django 4.1.7 on 2023-03-09 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('b2', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=155, verbose_name='Марка')),
                ('slug', models.SlugField(unique=True, verbose_name='URL_BRAND')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=155, verbose_name='Модель')),
                ('year', models.DateField(verbose_name='Год')),
                ('slug', models.SlugField(unique=True, verbose_name='URL_CAR')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b2.brand')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]