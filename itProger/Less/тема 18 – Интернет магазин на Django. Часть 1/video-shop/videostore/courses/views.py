from django.views.generic import ListView, DetailView, CreateView
from .models import Courses, Lesson
# from django.shortcuts import render


class HomePage(ListView):
    model = Courses
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx

class CoursesDetailPage(DetailView):
    model = Courses
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CoursesDetailPage, self).get_context_data(**kwargs)
        course = Courses.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx

class LessonDeteilPage(DetailView):
    model = Courses
    template_name = 'courses/lesson-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDeteilPage, self).get_context_data(**kwargs)
        course = Courses.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()
        lesson.video = lesson.video.split('/')[4]
        ctx['title'] = lesson
        ctx['lesson'] = lesson
        return ctx

class CourseAddPage(CreateView):
    model = Courses
    template_name = 'courses/add-course.html'
    fields = ['slug', 'title', 'desc', 'image']

    def get_context_data(self, **kwards):
        ctx = super(CourseAddPage, self).get_context_data(**kwards)
        ctx['title'] = 'Добавление курса'
        ctx['btn_text'] = 'Добавить курс'
        return ctx



class LessonAddPage(CreateView):
    model = Lesson
    template_name = 'courses/course-detail.html'
    fields = ['slug', 'title', 'desc', 'course', 'number', 'video']

    def form_valid(self, form):
        form.instance.desc = 'desc'
        return super().form_valid(form)

    # def get_context_data(self, **kwards):
    #     ctx = super(LessonAddPage, self).get_context_data(**kwards)
    #     ctx['title'] = 'Форма добавления урока'
    #     ctx['btn_text'] = 'Добавить урок'
    #     return ctx