from django.contrib.auth.models import AbstractUser
from django.db import models

from users.utils import create_token

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=50, **NULLABLE, verbose_name='фамилия')
    last_name = models.CharField(max_length=50, **NULLABLE, verbose_name='имя')
    token = models.CharField(max_length=100, default='token', verbose_name='token')
    email_verify = models.BooleanField(default=False, verbose_name='верификация почты')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        permissions = [
            (
                'set_email_verify',
                'Can email verify'
            ),
            (
                'set_is_active',
                'Can is active'
            )
        ]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

