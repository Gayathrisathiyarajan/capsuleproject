from django import forms
from .models import TimeCapsule

class TimeCapsuleForm(forms.ModelForm):
    class Meta:
        model = TimeCapsule
        fields = ['title', 'message', 'media', 'unlock_date', 'email']
        widgets = {
            'unlock_date': forms.DateInput(attrs={'type': 'date'}),
        }