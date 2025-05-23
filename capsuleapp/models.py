from django.db import models
from datetime import date

class TimeCapsule(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to='capsule_media/', blank=True, null=True)
    unlock_date = models.DateField()
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email_sent = models.BooleanField(default=False)
    def is_unlocked(self):
        return date.today() >= self.unlock_date

    def __str__(self):
        return self.title