from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email"), unique=True, max_length=254)
    
    @classmethod
    def create(cls, kwargs):
        if kwargs.get('is_superuser'):
            return cls.objects.create_superuser(**kwargs)
        return cls.objects.create_user(**kwargs)
