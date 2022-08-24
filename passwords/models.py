from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Password(models.Model):
    service = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    additional_info = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f"Password for {self.service} created by {self.author}"

    def get_absolute_url(self):
        return reverse('password-detail', kwargs={'pk': self.pk})
