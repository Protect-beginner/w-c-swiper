from django.conf.urls import url
from django.urls import path

from . import apis

urlpatterns = [
    path('vcode/fetch', apis.FetchView.as_view()),
    path('vcode/submit', apis.SubmitView.as_view()),
    path('profile/show', apis.ProfileShowView.as_view()),
    path('profile/update', apis.ProfileUpdateView.as_view()),
    path('qiniu/token', apis.QnTokenView.as_view()),
    path('qiniu/callback', apis.QnCallbackView.as_view()),
]
