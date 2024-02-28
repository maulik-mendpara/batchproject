from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields=['firstname','lastname','username','password','state','city','mobile']

class notesForm(forms.ModelForm):
    class Meta:
        model=notesdata
        fields='__all__'
        
class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'