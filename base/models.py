from django.contrib.auth.models import AbstractUser
from django.db import models 



class User(AbstractUser):
    # 'student' or 'teacher'
    student_or_teacher = models.CharField(max_length=7, null=False, default='student')
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    