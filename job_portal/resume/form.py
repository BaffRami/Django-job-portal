from django import forms
from .models import Resume

class ResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = {'user', }
        widgets = {
            'cv' : forms.FileInput(attrs={'accept':'.pdf'}),
        }