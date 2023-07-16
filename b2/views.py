from datetime import datetime

from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import *


class Brand(ListView):
    model = Brand
    template_name = 'b2/brands.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = '<a href="qwe">Toyota</a>'
        context['model'] = 'Supra'
        context['country'] = 'Не фурычит'
        context['errror'] = None
        context['one'] = 3.221421
        context['two'] = 2.2321421
        context['three'] = 5.324124
        context['four'] = 2512934213.3243289419234124
        context['five'] = -213213.00000
        context['now'] = datetime.now()
        context['text_str'] = "Здесь какой-то текст"
        context['text_str1'] = ["Здесь","какой","текст",'какой','неизвестно','но','текст']

        return context






# class Model(ListView):
#     model = Car
#     template_name = 'b2/models.html'
#     context_object_name = 'item'
#     slug_url_kwarg = 'slug'
#
#     def get_queryset(self):
#         return Brand.objects.all()
#         return Car.objects.filter(brand__slug=self.kwargs['slug'])

# class Car(DetailView):
#     model = Car
#     template_name = 'b2/models.html'
#     context_object_name = 'item'
#     slug_url_kwarg = 'slug'
