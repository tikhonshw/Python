from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField('Название статьи', max_length=100)
    text = models.TextField('Описание статьи')
    date = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete=models.CASCADE - удаляет связанные элементы из таблицы

    def __str__(self):
        return f'Новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
