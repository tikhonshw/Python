from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Feedback(models.Model):
    username = None
    theme = models.CharField('Тема письма', max_length=100)
    email = models.EmailField('Ваша почта', max_length=100)
    textMess = models.TextField('Текст сообщения')
    date = models.DateTimeField('Дата добавления', default=timezone.now)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'Тема обращения: {self.theme}'

    class Meta:
        verbose_name = 'Пиьмо пользователя'
        verbose_name_plural = 'Письма пользователей'


class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Описание статьи')
    date = models.DateTimeField(default=timezone.now)
    # on_delete=models.CASCADE - удаляет связанные элементы из таблицы
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.IntegerField('Просмотры', default=1)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
