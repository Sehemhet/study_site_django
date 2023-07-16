from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand','slug')

class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand','model', 'year', 'slug')


admin.site.register(Car, CarsAdmin)
admin.site.register(Brand, BrandAdmin)
# Register your models here.



