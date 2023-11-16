from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from student.models import Student
from teacher.models import Teacher
from .forms import RegistrationForm
# from django.contrib.auth.forms import UserCreationForm

def is_authenticated(view_function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated: 
            view_function(request, *args, **kwargs)
        else:
            return redirect('base:login')
    return wrapper

def home_decorator(home_view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            User = get_user_model()
            user_type = User.objects.get(username=request.user)
            if user_type.student_or_teacher == 'student':
                return redirect('student:student_home')
            else:
                return redirect('teacher:teacher_home')
        else:
            return home_view(request, *args, **kwargs)
    return wrapper

@home_decorator
def home(request):
    return render(request, 'main/home.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                login(request, user)
            except:
                print('error logging in')
            User = get_user_model()
            user_type = User.objects.get(username=user)
            # UNNECESSARY? just redirect home and let decorator handle
            if user_type.student_or_teacher == 'student':
                return redirect('student:student_home')
            else:
                return redirect('teacher:teacher_home')
    return render(request, 'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect('base:home')

def registerStudent(request):
    print('student registration')
    user_form = RegistrationForm()
    if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                form.instance.student_or_teacher = 'student'

                # check teacher name / studio password
                teacher = request.POST.get('teacher')
                try:
                    teacher = Teacher.objects.get(name=teacher)
                except:
                    messages.error(request, 'TEACHER DOES NOT EXIST')
                    return render(request, 'base/register.html', {'form': user_form, 'role': 'student'})
                if teacher is not None:
                    print('teacher exists!')
                    student = Student(user=user, name='student', teacher=teacher)
                    user.save()
                    student.save()
                    login(request, user)
                    return redirect('base:home')

            else:
                print(form.error_messages)
                messages.error(request, form.error_messages)
    return render(request, 'base/register.html', {'form': user_form, 'role': 'student'})


def registerTeacher(request):
    print('teacher registration')
    user_form = RegistrationForm()
    if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.instance.student_or_teacher = 'teacher'
                user = form.save()
                user.save()
                login(request, user)
                return redirect('base:home')
            else:
                print(form.error_messages)
                messages.error(request, 'Error in registration.')
    return render(request, 'base/register.html', {'form': user_form, 'role': 'teacher'})
