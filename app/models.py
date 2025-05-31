from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone

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
        default=''
    )
    name = models.CharField(max_length=100, verbose_name='имя', default='')
    surname = models.CharField(max_length=100, verbose_name='фамилия', default='')
    patronymic = models.CharField(max_length=100, verbose_name='отчество', **NULLABLE)
    comment = models.TextField(verbose_name='комментарий', max_length=500, **NULLABLE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок', default='')
    body = models.TextField(max_length=5000, verbose_name='сообщение', blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Newsletter(models.Model):
    PERIODICITY_CHOICES = [
        ('day', 'Раз в день'),
        ('week', 'Раз в неделю'),
        ('month', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('launched', 'Запущена'),
        ('completed', 'Завершена')
    ]

    date_time = models.DateTimeField(verbose_name='дата и время рассылки', default=timezone.now)
    periodicity = models.CharField(choices=PERIODICITY_CHOICES, default='day',
                                   verbose_name='периодичность рассылки')
    status = models.CharField(choices=STATUS_CHOICES, default='created', verbose_name='статус')
    clients = models.ManyToManyField(Client, verbose_name='клиенты')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')

    def __str__(self):
        return self.date_time

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Attempt(models.Model):
    ATTEMPT_STATUS_CHOICES = [
        ('success', 'Успешно'),
        ('failed', 'Не успешно'),
    ]
    date_time = models.DateTimeField(verbose_name='дата и время последней попытки', default=timezone.now)
    status = models.CharField(choices=ATTEMPT_STATUS_CHOICES, default='success',
                              verbose_name='статус последней попытки')
    response = models.TextField(verbose_name='ответ сервера', **NULLABLE)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='попытка')

    def __str__(self):
        return f"Рассылка от {self.date_time}"

    class Meta:
        verbose_name = 'попытка'
        verbose_name_plural = 'попытки'
