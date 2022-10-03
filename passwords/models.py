from django.db import models
from django.contrib.auth.models import User
from django.db.models import DEFERRED
from django.utils import timezone
from django.urls import reverse

import cryptocode

DEFAULT_ICON = "https://w7.pngwing.com/pngs/285/477/png-transparent-web-development-web-design-internet-" \
               "web-hosting-service-world-wide-web-logo-symmetry-sphere.png"
ENCRYPTED_FIELDNAMES = ["service_icon_url", "service_name", "service_url", "password",
                        "username", "email", "additional_info"]


class Password(models.Model):
    user_key = None
    service_url = models.URLField(max_length=255, default='')
    service_icon_url = models.URLField(max_length=255, default=DEFAULT_ICON)
    service_name = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    username = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(max_length=255, blank=True, default='')
    additional_info = models.TextField(blank=True, default='')
    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f"Password for {self.service_url} created by {self.author}"

    def save(self, *args, **kwargs):
        self.service_icon_url = cryptocode.encrypt(self.get_icon_url(self.service_url), self.user_key)
        self.service_name = cryptocode.encrypt(self.get_service_name(self.service_url), self.user_key)
        self.service_url = cryptocode.encrypt(self.service_url, self.user_key)
        self.password = cryptocode.encrypt(self.password, self.user_key)
        self.username = cryptocode.encrypt(self.username, self.user_key)
        self.email = cryptocode.encrypt(self.email, self.user_key)
        self.additional_info = cryptocode.encrypt(self.additional_info, self.user_key)

        super(Password, self).save(*args, **kwargs)

    @classmethod
    def from_db(cls, db, field_names, values):
        if len(values) != len(cls._meta.concrete_fields):
            values_iter = iter(values)
            values = [
                next(values_iter) if f.attname in field_names else DEFERRED
                for f in cls._meta.concrete_fields
            ]

        for i, (fieldname, val) in enumerate(zip(field_names, values)):
            if fieldname in ENCRYPTED_FIELDNAMES:
                values[i] = cryptocode.decrypt(val, cls.user_key)

        new = cls(*values)
        new._state.adding = False
        new._state.db = db
        return new

    @staticmethod
    def get_icon_url(service_url):
        size = 128
        service_url = service_url.replace("https://", '').replace("http://", '')
        return f"http://empty-coffee-mole.faviconkit.com/{service_url}/{size}"

    @staticmethod
    def get_service_name(service_url):
        service_name = service_url.replace("https://", '').replace("http://", '').replace("www.", '')
        domain_name_start_index = -service_name[::-1].index('.') - 1
        service_name = service_name[:domain_name_start_index]
        service_name = service_name.capitalize()
        return service_name

    def get_absolute_url(self):
        return reverse('password-detail', kwargs={'pk': self.pk})
