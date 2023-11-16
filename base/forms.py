from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    student_or_teacher = forms.ChoiceField(choices=(('student', 'Student'), ('teacher', 'Teacher')))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'student_or_teacher')
