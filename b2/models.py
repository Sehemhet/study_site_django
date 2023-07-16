from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Car(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    model = models.CharField(max_length=155, verbose_name='Модель')
    year = models.DateField(verbose_name='Год')
    slug = models.SlugField(unique=True, verbose_name='URL_CAR')

    def get_absolute_url(self):
        return reverse('car', kwargs={"slug": self.slug})

    def __str__(self):
        return self.brand

    objects = models.Manager()

class Brand(models.Model):
    brand = models.CharField(max_length=155, verbose_name='Марка')
    slug = models.SlugField(unique=True, verbose_name='URL_BRAND')

    def get_absolute_url(self):
        return reverse('model', kwargs={"slug": self.slug})

    def __str__(self):
        return self.brand

    objects = models.Manager()


