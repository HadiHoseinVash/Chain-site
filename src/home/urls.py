from django.urls import path
from home.views import *

urlpatterns = [
    path("", Welcome.as_view()),
    path("hello/",Hello.as_view()),
]

