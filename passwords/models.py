from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django_cryptography.fields import encrypt
import random
import string


DEFAULT_ICON = "https://w7.pngwing.com/pngs/285/477/png-transparent-web-development-web-design-internet-" \
          "web-hosting-service-world-wide-web-logo-symmetry-sphere.png"


def generate_password():
    password_length = 16
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = "".join(random.sample(chars, password_length))
    return password


def get_icon_url(service_url):
    size = 128
    service_url = service_url.replace("https://", '').replace("http://", '')
    return f"http://empty-coffee-mole.faviconkit.com/{service_url}/{size}"


def get_service_name(service_url):
    service_name = service_url.replace("https://", '').replace("http://", '').replace("www.", '')
    last_dot_index = -service_name[::-1].index('.') - 1
    service_name = service_name[:last_dot_index]
    service_name = service_name.capitalize()
    return service_name


class Password(models.Model):
    service_url = encrypt(models.URLField(max_length=255, default=''))
    service_icon_url = encrypt(models.URLField(max_length=255, default=DEFAULT_ICON))
    service_name = encrypt(models.CharField(max_length=255, default=''))
    password = encrypt(models.CharField(max_length=255, default=''))
    username = encrypt(models.CharField(max_length=255, blank=True, default=''))
    email = encrypt(models.EmailField(max_length=255, blank=True, default=''))
    additional_info = encrypt(models.TextField(blank=True, default=''))
    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f"Password for {self.service_url} created by {self.author}"

    def save(self, *args, **kwargs):
        self.service_icon_url = get_icon_url(self.service_url)
        self.service_name = get_service_name(self.service_url)
        super(Password, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('password-detail', kwargs={'pk': self.pk})

