from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import *
from .models import *
from .forms import *


# Create your views here.


def index(request):
    return render(request, 'index.html', {})

class SubmittableAuthenticationView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class Administrator(ListView):
    template_name = 'administrator.html'
    model = Lesson
    context_object_name = 'lessons'

class LessonsDetailView(DetailView):
    template_name = 'lessons_detail.html'
    model = Lesson
    context_object_name = 'lesson'

class LessonsCreateView(CreateView):
    template_name = 'form.html'
    models = Lesson
    form_class = LessonForm
    success_url = reverse_lazy('administrator')


class LessonsUpdateView(UpdateView):
    template_name = 'form.html'
    model = Lesson
    form_class = LessonForm
    success_url = reverse_lazy('administrator')


class LessonsDeleteView(DeleteView):
    template_name = 'lessons_delete.html'
    model = Lesson
    form_class = LessonForm
    success_url = reverse_lazy('administrator')


def teacher(request):
    return render(request, 'teacher.html', {})


def student(request):
    return render(request, 'student.html', {})
