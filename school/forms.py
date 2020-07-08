from django.forms import *
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)

class SubmittableAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class LessonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Lesson
        fields = '__all__'

class MessageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Message
        fields = '__all__'

class StudentTestForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = StudentTest
        fields = '__all__'
