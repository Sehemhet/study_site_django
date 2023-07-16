
from django.urls import path, re_path
from .views import *

urlpatterns = [
    # path('/<slug:slug>', Car.as_view(), name='car'),
    # path('<slug:<slug>', Model.as_view(), name='model'),
    path('', Brand.as_view(), name='brand'),
]