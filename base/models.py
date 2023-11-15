from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.apps import apps


class User(AbstractUser):
    # 'student' or 'teacher'
    student_or_teacher = models.CharField(max_length=7, null=False, default='student')
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            print('saving...')
            super(User, self).save(*args, **kwargs)
            print('saved')
            if self.student_or_teacher == 'student':
                Student = apps.get_model('student', 'Student')
                user = self
                Student.objects.create(user=user, name=self.username)
        else:
            super(User, self).save(*args, **kwargs)