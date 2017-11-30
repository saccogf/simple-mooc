from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Username', max_length=30, unique=True)
    email = models.EmailField('E-mail', unique=True)
    first_name = models.CharField('First Name', max_length=100, blank=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True)
    is_active = models.BooleanField('Is Active?', blank=True, default=True)
    is_staff = models.BooleanField('Is Staff?', blank=True, default=False)
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.first_name or self.username

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
