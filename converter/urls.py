from django.urls import path
from converter.views import currency_converter_view

urlpatterns = [
    path('', currency_converter_view, name='currency-converter'),
]