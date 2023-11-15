from django.shortcuts import render

# NEXT: Decorator to make sure user is student

def student_home(request):
    context
    return render(request, 'student/student_home.html', context={'student_or_teacher': 'student'})


def practice_entry(request):
    return render(request, 'student/practice_entry.html')
