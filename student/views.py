from django.shortcuts import render

def student_home(request):
    return render(request, 'student_home.html')