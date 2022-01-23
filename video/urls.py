from django.urls import path
from .views import *

app_name='video'

urlpatterns=[
    path('',video_list, name='list'),
    path('new/',video_new),
    path('<video_id>/', video_detail),
]