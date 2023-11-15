from django.db import models
from django.forms import ModelForm
from models import PracticeEntry

class PracticeForm(ModelForm):
    model = PracticeEntry
    fields = ["time", 'notes']