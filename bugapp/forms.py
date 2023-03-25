from django import forms
from bugapp import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields ="__all__"  

class Customer(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields ="__all__"
        




