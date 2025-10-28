from django import forms
from django.core.exceptions import ValidationError

from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = 'first_name', 'last_name', 'birthday', 'image', 'teacher'
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date'}, format='%Y-%m-%d'
            ),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
