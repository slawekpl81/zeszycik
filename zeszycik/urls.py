"""zeszycik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from school import views
from school.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    #path('', views.newsignup, name='test'),
    path('', UsersCreate.as_view(), name='test'),
    #path('', views.newsignin),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='test'), name='logout'),
    path('accounts/profile/', dashboard, name='dashboard'),

    path('users', UsersListView.as_view(), name='users_list'),
    path('users/update/<pk>', UsersUpdateView.as_view(), name='user_update'),

    path('administrator', Administrator.as_view(), name='administrator'),


    path('lessons', LessonsListView.as_view(), name='lessons_list'),
    path('lesson/detail/<pk>', LessonsDetailView.as_view(), name='lesson_detail'),
    path('lesson/data/<pk>', LessonsDataView.as_view(), name='lesson_data'),
    path('lesson/update/<pk>', LessonsUpdateView.as_view(), name='lesson_update'),
    path('lesson/delete/<pk>', LessonsDeleteView.as_view(), name='lesson_delete'),
    path('lessons/create',     LessonsCreateView.as_view(), name='lesson_create'),
    path('lessons/addstudent/<pk>', LessonsAddStudentView.as_view(), name='lesson_add_student'),

    path('messages', MessageListView.as_view(), name='messages_list'),
    path('message/detail/<pk>', MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<pk>', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('message/create',      MessageCreateView.as_view(), name='message_create'),

    path('studenttests', StudentTestListView.as_view(), name='studenttest_list'),
    path('studenttest/detail/<pk>', StudentTestDetailView.as_view(), name='studenttest_detail'),
    path('studenttest/update/<pk>', StudentTestUpdateView.as_view(), name='studenttest_update'),
    path('studenttest/delete/<pk>', StudentTestDeleteView.as_view(), name='studenttest_delete'),
    path('studenttest/create',      StudentTestCreateView.as_view(), name='studenttest_create'),
    path('studenttest/solve',       StudentTestSolveView.as_view(), name='studenttest_solve'),
    path('studenttest/solve/<pk>',  StudentTestSolveUpdateView.as_view(),  name='studenttest_solve_update'),
    path('exams',                   ExamListView.as_view(),  name='exams'),

    path('calendar', CalendarView.as_view(), name='calendar'),
    path('library', LibraryView.as_view(), name='library'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


