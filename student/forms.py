from django.db import models
from django.forms import ModelForm
from .models import PracticeEntry, Student


class PracticeForm(ModelForm):
    class Meta:
        model = PracticeEntry
        fields = ["time", 'notes']