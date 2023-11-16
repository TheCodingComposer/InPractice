from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.apps import apps


class User(AbstractUser):
    # 'student' or 'teacher'
    student_or_teacher = models.CharField(max_length=7, null=False, default='student')
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         print('saving...')
    #         super(User, self).save(*args, **kwargs)
    #         print('saved')
    #         if self.student_or_teacher == 'student':
    #             student = apps.get_model('student', 'Student')
    #             student.objects.create(user=self, name=self.username)
    #         else:
    #             teacher = apps.get_model('teacher', 'Teacher')
    #             teacher.objects.create(user=self, name=self.username)
    #     else:
    #         super(User, self).save(*args, **kwargs)
