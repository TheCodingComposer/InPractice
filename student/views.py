from django.shortcuts import render, redirect
from .forms import PracticeForm
from base.models import User
from .models import Student
from django.contrib.auth import get_user_model

# NEXT: Decorator to make sure user is student

def student_home(request):

    return render(request, 'student/student_home.html', context={'student_or_teacher': 'student'})


def practice_entry(request):
    if request.method == "POST":
        form = PracticeForm(request.POST)
        if form.is_valid():
            student = Student.objects.get(user=request.user)
            form.instance.student = student
            form.save()
            return redirect('student:student_home')
        else:
            print('error')

    form = PracticeForm()
    return render(request, 'student/practice_entry.html', context={'form': form})
