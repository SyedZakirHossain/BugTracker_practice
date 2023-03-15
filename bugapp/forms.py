from django import forms
from bugapp import models



class Customer(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields ="__all__"
        



"""
from .models import User



        
class Homework(forms.ModelForm):
    class Meta:
        model = models.Homework
        fields ="__all__"
        
class Contact(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields ="__all__"        
class User(forms.ModelForm):
    class Meta:
        model = models.User
        fields ="__all__"   
        """
