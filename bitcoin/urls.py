from django.urls import path
from bitcoin.views import (
    bitcoinAPI,
    index,
)


urlpatterns=[
    path('', index, name='index'),
    path('test/', bitcoinAPI, name='bitcoin'),

]