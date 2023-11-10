from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    student_or_teacher = forms.ChoiceField(choices=(('student', 'Student'), ('teacher', 'Teacher')))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'student_or_teacher')
    #     fields = (
    #         'username',
    #         'first_name',
    #         'last_name',
    #         'email',
    #         'password1',
    #         'password2'
    #     )

    #     def save(self, commit = True):
    #         user = super(RegistrationForm, self).save(commit= False)
    #         user.first_name = self.cleaned_data['first_name']
    #         user.last_name = self.cleaned_data['last_name']
    #         user.email = self.cleaned_data['email']

    #         if commit:
    #             user.save()

    #             return User