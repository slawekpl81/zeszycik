from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class SchoolUser(models.Model):
    USERS_KIND = [
        ('administrator', 'Dyrektor'),
        ('teacher', 'Nauczyciel'),
        ('student', 'Uczeń')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    permissions = models.CharField(choices=USERS_KIND, max_length=15)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.permissions}'


class Lesson(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False)
    description = models.TextField()
    teacher = models.ForeignKey(SchoolUser, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    data = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(SchoolUser, on_delete=models.DO_NOTHING, related_name='author')
    target = models.ForeignKey(SchoolUser, on_delete=models.DO_NOTHING, related_name='target')
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'OD:{self.author} DO:{self.target} Z: {self.created}'

