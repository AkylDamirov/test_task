from django import forms
from .models import Cities

class CitiesForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ('city',)


