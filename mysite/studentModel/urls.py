from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.middleware import AuthenticationMiddleware

urlpatterns = [
    path('private/addPersonality', AddPersonality.as_view()),
    path('private/getPersonality', GetPersonality.as_view()),
    path('private/editPersonality', PutPersonality.as_view()),
]