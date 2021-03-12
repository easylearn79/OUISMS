from django import forms
from .models import StudentInfo

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Academic Year'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Admission Date'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission ID'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full_Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'dept_name': forms.Select(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'shift_type': forms.Select(attrs={'class': 'form-control'}),
            'fees': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'TOTAL FEES'}),
            'level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LEVEL'}),
        }

