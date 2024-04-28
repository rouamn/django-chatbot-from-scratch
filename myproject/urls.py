# urls.py
from django.contrib import admin
from django.urls import path
from .chatbotView import chat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', chat, name='chatbot'),
]
