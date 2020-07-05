from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class SchoolUser(models.Model):
    USERS_KIND = [
        ('administrator', 'Administrator'),
        ('teacher', 'Teacher'),
        ('student', 'Student')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, unique=True, blank=False)
    permissions = models.CharField(choices=USERS_KIND, max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False)
    description = models.TextField()
    teacher = models.ForeignKey(SchoolUser, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()


# class Message(models.Model):
#     author = models.ForeignKey(SchoolUser, on_delete=models.DO_NOTHING)
#     target = models.ForeignKey(SchoolUser, on_delete=models.DO_NOTHING)
#     text = models.TextField()
