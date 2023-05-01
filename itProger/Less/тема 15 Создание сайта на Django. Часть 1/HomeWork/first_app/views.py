from django.shortcuts import render
# from .models import News


def home(request):
    return render(request, 'first_app/home.html', {'title': 'Главная страница'})


def uslugi(request):
    return render(request, 'first_app/uslugi.html', {'title': 'Услуги'})


def contact(request):
    return render(request, 'first_app/contact.html', {'title': 'Контакты'})


def about(request):
    return render(request, 'first_app/about.html', {'title': 'Про нас'})
