from django.conf.urls import url
from django.urls import path

from . import apis

urlpatterns = [
    path('rcmd', apis.rcmd_users),
    path('like', apis.like),
    path('superlike', apis.super_like),
    path('dislike', apis.dislike),
]
