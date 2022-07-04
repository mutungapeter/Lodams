from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', "user", "email", "phone_number", "course", "subject", "staff", "adm_number"]