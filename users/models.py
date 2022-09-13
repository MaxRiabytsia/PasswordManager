from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_theme = models.CharField(max_length=255, default='light', choices=[('light', 'Light Theme'),
                                                                                 ('dark', "Dark Theme")
                                                                                 ])

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
