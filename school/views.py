from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def administrator(request):
    return render(request, 'administrator.html', {})

def teacher(request):
    return render(request, 'teacher.html', {})

def student(request):
    return render(request, 'student.html', {})