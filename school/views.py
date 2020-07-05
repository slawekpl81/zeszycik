from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class Administrator(ListView):
    template_name = 'administrator.html'
    model = Lesson
    context_object_name = 'lessons'


class LessonsCreateView(CreateView):
    template_name = 'form.html'
    models = Lesson
    form_class = LessonForm
    success_url = reverse_lazy('administrator')


class LessonsUpdateView(UpdateView):
    pass


class LessonsDeleteView(DeleteView):
    pass


def teacher(request):
    return render(request, 'teacher.html', {})


def student(request):
    return render(request, 'student.html', {})
