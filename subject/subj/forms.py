from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

        widgets = {
            "subject_name": forms.TextInput(attrs={'class': 'form-control'}),
            "total_contents": forms.NumberInput(attrs={'class': 'form-control'}),
            "total_poems": forms.NumberInput(attrs={'class': 'form-control'}),
            "subject_teacher": forms.TextInput(attrs={'class': 'form-control'}),
            "study_mode": forms.Select(attrs={'class': 'form-control'}),
        }
