from django.forms import *
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from crispy_forms import *


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)


class SubmittableAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LessonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset= User.objects.filter(groups__name='students')
        self.fields['teacher'].queryset = User.objects.filter(groups__name='teachers')

    class Meta:
        model = Lesson
        fields = '__all__'


class MessageForm(ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['author'].queryset = User.objects.filter(username=user)

    class Meta:
        model = Message
        fields = '__all__'


class StudentTestForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.filter(groups__name='teachers')

    class Meta:
        model = StudentTest
        fields = '__all__'


class StudentTestSolveForm(ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['student'].queryset = User.objects.filter(username=user)

    class Meta:
        model = Exam
        fields = '__all__'
