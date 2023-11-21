from django import forms
from .models import*
class doctorform(forms.ModelForm):
    class Meta:
        model=doctor
        fields='__all__'