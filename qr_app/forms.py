from django import forms
from django.forms import ModelForm

from .models import *

class QrForm(forms.ModelForm):

    class Meta:
        model = QrInfo
        fields= ['info']