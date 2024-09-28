from django import forms
from .models import MediaDetail, Quote

class UserInfoForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = []  # No fields needed if the hash is generated automatically

class MediaDetailForm(forms.ModelForm):
    class Meta:
        model = MediaDetail
        fields = ['quote', 'type', 'quantity', 'condition']