from datetime import datetime

from django.db import models
from django.utils.timezone import now

from service.const import PERIODIC_CHOICES, DAY, STATUS_CHOICES, NO_ACTIVE
from users.models import NULLABLE


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=150, **NULLABLE, verbose_name='имя')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')
    author = models.ForeignKey('users.User', **NULLABLE, on_delete=models.CASCADE, verbose_name='автор')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Massage(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема')
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    massage = models.ForeignKey(Massage, **NULLABLE, on_delete=models.CASCADE, verbose_name='сообщение')
    periodic = models.IntegerField(choices=PERIODIC_CHOICES, default=DAY, verbose_name='периодичность')
    start = models.DateTimeField(default=datetime.now, verbose_name='начало')
    stop = models.DateTimeField(default=datetime.now, verbose_name='окончание')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NO_ACTIVE, verbose_name='статус')
    clients = models.ManyToManyField(Client, blank=True, verbose_name='клиенты')
    author = models.ForeignKey('users.User', **NULLABLE, on_delete=models.CASCADE, verbose_name='автор')
    is_active = models.BooleanField(default=False, verbose_name='активна')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        permissions = [
            ('set_start_mailing', 'Can start mailing'),
            ('set_activat_mailing', 'Can activate mailing')
        ]


class Log(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    time_attempt = models.DateTimeField(default=now, verbose_name='время последней попытки')
    status = models.CharField(max_length=100, verbose_name='статус')
    mode = models.CharField(max_length=100, verbose_name='режим')
    mail_server_response = models.CharField(max_length=100, **NULLABLE, verbose_name='ответ почтового сервера')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
