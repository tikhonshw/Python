from django.db import models
from django.urls import reverse

# Create your models here.
class Courses(models.Model):
    slug = models.SlugField('Уникальное название курса', unique=True)
    title = models.CharField('Название курса', max_length=120)
    desc = models.TextField('Описание курса')
    image = models.ImageField('Изображение', default='default.png', upload_to='course_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})


class Lesson(models.Model):
    slug = models.SlugField('Уникальное название урока')
    title = models.CharField('Название урока', max_length=120)
    desc = models.TextField('Описание урока')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Какой курс?')
    number = models.IntegerField('Номер урока')
    video = models.CharField('Ссылка на видео урок', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})