from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
            'phoneNumber',
            'bio',
            'picture'
        ]
        widgets={
            'phoneNumber':forms.TextInput(attrs={'placeholder':'Enter phone number'}),
            'bio':forms.Textarea(attrs={
                'placeholder':'Enter bio'
            })

        }
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter username'}),
            'email':forms.EmailInput(
                attrs={'placeholder':'Your email address'}
            ),
        }