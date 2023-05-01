from django.urls import path
from . import views

urlpatterns = [
    # path('', include('courses.urls'))
    path('', views.HomePage.as_view(), name = 'home'),
    path('course/<slug>/', views.CoursesDetailPage.as_view(), name='course-detail'),
    path('course/<slug>/<lesson_slug>', views.LessonDeteilPage.as_view(), name='lesson-detail'),
    path('add-course', views.CourseAddPage.as_view(), name='add-course'),
    path('add-lesson', views.LessonAddPage.as_view(), name='add-lesson')

]
