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


class Administrator(ListView):
    template_name = 'administrator.html'
    model = Lesson
    context_object_name = 'lessons'


# ============================================================================================
class LessonsListView(ListView):
    template_name = ''
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


# ============================================================================================
class MessageListView(ListView):
    template_name = ''
    model = Message
    context_object_name = 'messages'

    # def get_context_data(self, *args, object_list=None, **kwargs):
    #     context = super(MessageListView, self).get_context_data(*args, **kwargs)
    #
    #     login_user = User.objects.filter(user=self.request.user)



class MessageDetailView(DetailView):
    template_name = 'message_detail.html'
    model = Message
    context_object_name = 'message'


class MessageCreateView(CreateView):
    template_name = 'form.html'
    models = Message
    form_class = MessageForm
    success_url = reverse_lazy('administrator')


class MessageUpdateView(UpdateView):
    template_name = 'form.html'
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('administrator')


class MessageDeleteView(DeleteView):
    template_name = 'message_delete.html'
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('administrator')


# ============================================================================================

class StudentTestDetailView(DetailView):
    template_name = 'studenttest_detail.html'
    model = StudentTest
    context_object_name = 'test'


class StudentTestCreateView(CreateView):
    template_name = 'form.html'
    models = StudentTest
    form_class = StudentTestForm
    success_url = reverse_lazy('administrator')


class StudentTestUpdateView(UpdateView):
    template_name = 'form.html'
    model = StudentTest
    form_class = StudentTestForm
    success_url = reverse_lazy('administrator')


class StudentTestDeleteView(DeleteView):
    template_name = 'studenttest_delete.html'
    model = StudentTest
    form_class = StudentTestForm
    success_url = reverse_lazy('administrator')


# ============================================================================================
def teacher(request):
    return render(request, 'teacher.html', {})


def student(request):
    return render(request, 'student.html', {})
