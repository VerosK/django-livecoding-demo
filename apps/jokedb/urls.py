# apps/jokedb/urls.py

from django.urls import path
from .views import index, show_joke

urlpatterns = [
    path('', index),
    path('joke/<int:joke_id>/', show_joke),
]
