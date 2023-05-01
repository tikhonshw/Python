from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import News
from .forms import FeedbackForm
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.core.mail import send_mail


#
# def home(request):
#     data = {
#         'news': News.objects.all(),
#         'title': 'Главная страница'
#     }
#     return render(request, 'blog/home.html', data)


class DeleteNewsView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    # ordering = ['-date']
    paginate_by = 1

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(autor=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)
        ctx['title'] = f"Статьи от пользователя {self.kwargs.get('username')}"
        return ctx


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        # ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
        # ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить новость'
        return ctx


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)
        # ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить новость'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False


def about(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Ваше сообщение сохранено\nДополнительно направлено пиьсмо администратору сайта')

            theme = form.cleaned_data.get('theme')
            email = form.cleaned_data.get('email')
            textMess = form.cleaned_data.get('textMess')

            subject = "На сайте добавлено новое обращение"
            plain_message = f"Добрый день!\nПоступило новоое обращения:\n\nТема:{theme}\n\nСообщение:\n{textMess}\n\nот: {email}"
            from_email = f"From <{email}>"
            to = "tikhonshw@gmail.com"
            send_mail(subject, plain_message, from_email, [to])

            # return redirect('home')
    else:
        form = FeedbackForm()

    return render(
        request,
        'blog/contact.html',
        {
            'title': 'Страницы обратной связи',
            'form': form
        }
    )
