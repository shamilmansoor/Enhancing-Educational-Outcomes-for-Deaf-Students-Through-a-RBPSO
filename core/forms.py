from django import forms
from .models import Student, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name', 'student_id', 'age', 'sex', 'address', 'hearing_loss',
            'school_support', 'paid_classes', 'ia1', 'ia2', 'ia3',
            'nursery_attendance', 'internet_access', 'study_time',
            'extracurricular', 'absences'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Select(attrs={'class': 'form-control'}),
            'hearing_loss': forms.Select(attrs={'class': 'form-control'}),
            'school_support': forms.Select(attrs={'class': 'form-control'}),
            'paid_classes': forms.Select(attrs={'class': 'form-control'}),
            'ia1': forms.NumberInput(attrs={'class': 'form-control'}),
            'ia2': forms.NumberInput(attrs={'class': 'form-control'}),
            'ia3': forms.NumberInput(attrs={'class': 'form-control'}),
            'nursery_attendance': forms.Select(attrs={'class': 'form-control'}),
            'internet_access': forms.Select(attrs={'class': 'form-control'}),
            'study_time': forms.Select(attrs={'class': 'form-control'}),
            'extracurricular': forms.Select(attrs={'class': 'form-control'}),
            'absences': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Teacher
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        } 