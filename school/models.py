from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from functools import reduce


# Create your models here.


class SchoolUser(models.Model):
    # USERS_KIND = [
    #     ('administrator', 'Dyrektor'),
    #     ('teacher', 'Nauczyciel'),
    #     ('student', 'Uczeń')
    # ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # permissions = models.CharField(choices=USERS_KIND, max_length=15)
    grades = models.CharField(max_length=150, default='')

    def add_grade(self, grade):
        self.grades += str(grade)

    def mean_of_grades(self):
        mean = reduce(lambda sum_of, grade: int(sum_of) + int(grade), self.grades) / len(self.grades)
        return f'{mean :.2f}'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.user.groups[0].name}'


class Lesson(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False)
    description = models.CharField(max_length=250)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='teacher')
    date = models.DateTimeField(default=timezone.now)
    data = models.FileField(blank=True, null=True)
    students = models.ManyToManyField(User, null=True, blank=True, related_name='students')

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='author')
    target = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='target')
    text = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'OD:{self.author} DO:{self.target} Z: {self.created}'


class StudentTest(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=250)
    answer_right = models.CharField(max_length=5, default='')
    answer_1 = models.CharField(max_length=150, default='')
    answer_2 = models.CharField(max_length=150, default='')
    answer_3 = models.CharField(max_length=150, default='')
    answer_4 = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'{self.lesson.name}-{self.question[:30]}'



class Exam(models.Model):
    test = models.ForeignKey(StudentTest, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=5)
    passed_exam = models.BooleanField(default=False)

    @property
    def passed(self):
        if self.answer == self.test.answer_right:
            self._passed = True
        else:
            self._passed = False

        self.passed_exam = self._passed
        self.save()
        return self._passed

    def __str__(self):
        return f'{self.student} - {self.passed}'
