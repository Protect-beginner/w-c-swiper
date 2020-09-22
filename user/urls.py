from django.urls import path
from . import views

urlpatterns = [
    path('vcode/fetch/', views.Userland.as_view()),
]
