from django.urls import path

from .views import *

app_name='search'

urlpatterns=[
    path('',indexx, name='search'),
    path('blog/',blog),
    path('garen/',garen),
    path('ashe/',ashe),
]