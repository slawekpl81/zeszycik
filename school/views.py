from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from school.forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

def newsignup(request):
    return render(request, 'index.html', {"formSignup": UserCreationForm})


def newsignin(request):
    return render(request, 'index.html', {"formSignin": UserCreationForm})


def index(request):
    return render(request, 'index.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})


class Administrator(LoginRequiredMixin, ListView):
    template_name = 'administrator.html'
    model = Lesson
    context_object_name = 'lessons'


# ============================================================================================
class UsersCreate(CreateView,SuccessMessageMixin):
    template_name = 'index.html'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('test')
    success_message = "Your account was created successfully"

    def register(response):
            if response.method == "POST":
                form_class = RegistrationForm(response.POST)
                if form_class.is_valid():
                    form_class.save()
                    messages.success(request, 'Your account....')
                return redirect("index.html")
            else:
                form_class = RegistrationForm()
            return render(response, "index.html", {"form": form_class})


class UsersListView(LoginRequiredMixin, ListView):
    template_name = 'users.html'
    model = User
    context_object_name = 'users'


class UsersUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = User
    form_class = UsersUpdateForm
    success_url = reverse_lazy('users_list')


# ============================================================================================
class AddGradeView(FormView):
    template_name = 'form.html'
    form_class = AddGradeForm

    # def form_valid(self, form):
    #     result = super(AddGradeView, self).form_valid()
    #     login_user = self.request.user
    #     if not SchoolUser.objects.filter(user=login_user):
    #         SchoolUser.objects.create(user=login_user)
    #     s_user = SchoolUser.objects.filter(user=login_user)
    #     s_user.add_grade(cleaned_data)


# ============================================================================================
class LessonsListView(LoginRequiredMixin, ListView):
    template_name = 'lessons_list.html'
    model = Lesson
    context_object_name = 'lessons'


class LessonsDetailView(DetailView):
    template_name = 'lessons_detail.html'
    model = Lesson
    context_object_name = 'lesson'


class LessonsDataView(LoginRequiredMixin, DetailView):
    template_name = 'lessons_data.html'
    model = Lesson
    context_object_name = 'lesson'


class LessonsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    models = Lesson
    form_class = LessonForm
    success_url = reverse_lazy('lessons_list')


class LessonsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Lesson
    form_class = LessonForm
    success_url = reverse_lazy('lessons_list')


class LessonsAddStudentView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Lesson
    form_class = LessonAddStudentForm

    # success_url = reverse_lazy('lessons_list')

    def get_success_url(self):
        user = self.request.user
        lesson = self.object
        lesson.students.add(user)
        lesson.save()
        return reverse_lazy('lessons_list')


class LessonsDeleteView(DeleteView):
    template_name = 'lessons_delete.html'
    model = Lesson
    form_class = LessonForm
    success_url = reverse_lazy('lessons_list')


# ============================================================================================
class MessageListView(LoginRequiredMixin, ListView):
    template_name = 'messages_list.html'
    model = Message
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(target=self.request.user)


class MessageDetailView(DetailView):
    template_name = 'message_detail.html'
    model = Message
    context_object_name = 'message'


class MessageCreateView(CreateView):
    template_name = 'form.html'
    models = Message
    form_class = MessageForm
    success_url = reverse_lazy('messages_list')

    def get_form_kwargs(self):
        form = super(MessageCreateView, self).get_form_kwargs()
        form['user'] = self.request.user.username
        return form


class MessageUpdateView(UpdateView):
    template_name = 'form.html'
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('messages_list')


class MessageDeleteView(DeleteView):
    template_name = 'message_delete.html'
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('messages_list')


# ============================================================================================

class StudentTestListView(ListView):
    template_name = 'studenttest_list.html'
    model = StudentTest
    context_object_name = 'studenttests'


class StudentTestDetailView(DetailView):
    template_name = 'studenttest_detail.html'
    model = StudentTest
    context_object_name = 'test'


class StudentTestCreateView(CreateView):
    template_name = 'form.html'
    models = StudentTest
    form_class = StudentTestForm
    success_url = reverse_lazy('studenttest_list')


class StudentTestUpdateView(UpdateView):
    template_name = 'form.html'
    model = StudentTest
    form_class = StudentTestForm
    success_url = reverse_lazy('studenttest_list')


class StudentTestDeleteView(DeleteView):
    template_name = 'studenttest_delete.html'
    model = StudentTest
    form_class = StudentTestForm
    success_url = reverse_lazy('studenttest_list')


class StudentTestSolveView(CreateView):
    template_name = 'studenttest_solve.html'
    model = Exam
    form_class = StudentTestSolveForm

    def get_form_kwargs(self):
        form = super(StudentTestSolveView, self).get_form_kwargs()
        form['user'] = self.request.user.username
        return form

    def get_success_url(self):
        test_id = self.object.id
        return reverse_lazy('studenttest_solve_update', kwargs={'pk': test_id})


class StudentTestSolveUpdateView(UpdateView):
    template_name = 'studenttest_solve_update.html'
    model = Exam
    form_class = StudentTestSolveUpdateForm
    success_url = reverse_lazy('exams')

    def get_context_data(self, **kwargs):
        context = super(StudentTestSolveUpdateView, self).get_context_data(**kwargs)
        context['test'] = StudentTest.objects.filter(id=self.object.test.id)
        print(f'test!!!-{context["test"]}')
        return context


class ExamListView(LoginRequiredMixin, ListView):
    template_name = 'exam_list.html'
    model = Exam
    context_object_name = 'exams'

    def get_queryset(self):
        return Exam.objects.filter(student=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ExamListView, self).get_context_data()
        all_exam = Exam.objects.filter(student=self.request.user)
        ok_exam = Exam.objects.filter(student=self.request.user).filter(passed_exam=True)
        if len(all_exam):
            efficiency = len(ok_exam) / len(all_exam) * 100
            context['efficiency'] = f'{efficiency:.2f}'
        else:
            context['efficiency'] = f'No results!'
        return context


# ============================================================================================
class CalendarView(LoginRequiredMixin, ListView):
    template_name = 'calendar.html'
    model = Lesson
    context_object_name = 'lessons'


# ============================================================================================
class LibraryView(LoginRequiredMixin, ListView):
    template_name = 'library.html'
    model = Lesson
    context_object_name = 'books'


# ============================================================================================
def teacher(request):
    return render(request, 'teacher.html', {})


def student(request):
    return render(request, 'student.html', {})
