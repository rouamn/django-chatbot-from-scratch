# urls.py
from django.contrib import admin
from django.urls import path
from .chatbotView import chat
from .summarizerViews import summarize
from .pdfsummarizerViews import summarize_pdf_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', chat, name='chatbot'),
    path('summarize/', summarize, name='summarize'),
    path('summarize-pdf/', summarize_pdf_view, name='summarize_pdf'),
    
]
