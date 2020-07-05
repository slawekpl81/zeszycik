from django.forms import ModelForm
from .models import *


class LessonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Lesson
        fields = '__all__'
