from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True,
}


# Create your models here.
class Client(models.Model):
    email = models.EmailField(
        validators=[MinLengthValidator(5, 'Email должен быть от 5 до 254 символов'),
                    MaxLengthValidator(254, 'Email должен быть от 5 до 254 символов')],
        verbose_name='электронная почта',
        unique=True,
        **NULLABLE
    )
    name = models.CharField(max_length=100, verbose_name='имя', **NULLABLE)
    surname = models.CharField(max_length=100, verbose_name='фамилия', **NULLABLE)
    patronymic = models.CharField(max_length=100, verbose_name='отчество')
    comment = models.TextField(verbose_name='комментарий', max_length=500)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Newsletter(models.Model):
    PERIODICITY_CHOICES = {
        ('day', 'раз в день'),
        ('week', 'раз в неделю'),
        ('month', 'раз в месяц'),
    }

    STATUS_CHOICES = {
        ('created', 'создана'),
        ('launched', 'запущена'),
        ('completed', 'завершена')
    }

    date_time = models.DateTimeField(verbose_name='дата и время рассылки', **NULLABLE)
    periodicity = models.CharField(choices=PERIODICITY_CHOICES, default='day',
                                   verbose_name='периодичность рассылки')
    status = models.CharField(choices=STATUS_CHOICES, default='created', verbose_name='статус')

    def __str__(self):
        return self.date_time

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок', **NULLABLE)
    body = models.TextField(max_length=5000, verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Attempt(models.Model):
    ATTEMPT_STATUS_CHOICES = {
        ('success', 'успешно'),
        ('failed', 'не успешно'),
    }

    date_time = models.DateTimeField(verbose_name='дата и время последней попытки', **NULLABLE)
    status = models.CharField(choices=ATTEMPT_STATUS_CHOICES, default='success',
                              verbose_name='статус последней попытки')
    response = models.TextField(verbose_name='ответ сервера')

    def __str__(self):
        return self.date_time

    class Meta:
        verbose_name = 'попытка'
        verbose_name_plural = 'попытки'
