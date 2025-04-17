# core/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    phone = forms.CharField(label="Phone", max_length=20, required=False)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)
