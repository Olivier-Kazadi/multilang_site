#mains/urls.py
from django.urls import path
from .views import article_list, chatbot

urlpatterns = [
    path('', article_list, name='article_list'),
    path('chatbot/', chatbot, name='chatbot'),
]