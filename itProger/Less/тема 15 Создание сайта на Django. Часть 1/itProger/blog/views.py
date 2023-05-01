from django.shortcuts import render
from .models import News


def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'blog/home.html', data)


def about(request):
    return render(request, 'blog/contact.html', {'title': 'Страницы о нас'})
