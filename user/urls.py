from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('vcode/fetch/', views.FetchView.as_view()),
    path('vcode/submit/', views.SubmitView.as_view()),
    path('profile/show/', views.ProfileShowView.as_view()),
]
