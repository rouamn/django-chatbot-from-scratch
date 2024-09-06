# urls.py
from django.contrib import admin
from django.urls import path
from .chatbotView import chat
from .speechview import speech_to_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', chat, name='chatbot'),
       path('speech-to-text/', speech_to_text, name='speech_to_text'),
]