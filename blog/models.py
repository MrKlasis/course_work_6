from django.db import models
from django.utils.datetime_safe import date

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержимое', **NULLABLE)
    img = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    date_begin = models.DateField(default=date.today, verbose_name='Дата создания')
    activate = models.BooleanField(default=True)
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'