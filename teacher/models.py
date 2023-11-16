from django.db import models
from django.contrib.auth import get_user_model


class Teacher(models.Model):
    User = get_user_model()
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=50, default=user)
    studio_name = models.CharField(max_length=50, blank=False)
    studio_password = models.CharField(max_length=50, default='', blank=True)
    joined = models.TimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

