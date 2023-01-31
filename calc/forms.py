from django import forms
from.models import Hotel


class Hotel_form(forms.ModelForm):
    class Meta:
        model=Hotel
        fields=('name','price','location')
    