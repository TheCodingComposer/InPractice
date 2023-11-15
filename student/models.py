from django.db import models
from django.core.validators import MaxValueValidator
from base.models import User
from django.contrib.auth import get_user_model


class Student(models.Model):
    User = get_user_model()
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=50, default=user)
    joined = models.TimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name
class PracticeEntry(models.Model):
    # Practice time in minutes
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    time = models.IntegerField(validators=[MaxValueValidator(1440)])
    notes = models.TextField(max_length=500)
    created = models.TimeField(auto_now_add=True, editable=False)
    modified = models.TimeField(auto_now=True)