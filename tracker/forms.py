from django import forms
from django.forms.widgets import DateInput, TimeInput

from .models import Medicine


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        exclude = ('user',)
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'})
        }
