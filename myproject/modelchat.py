from django.db import models

class Chatbot(models.Model):
    chatId = models.CharField(max_length=100, null=True, blank=True)
    senderId = models.CharField(max_length=100, null=True, blank=True)
    messageType = models.CharField(max_length=20, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat ID: {self.chatId}, Sender ID: {self.senderId}, Content: {self.content}"
