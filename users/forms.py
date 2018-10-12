# users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput

from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'is_patient', 'is_doctor','password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'First Name (Required)'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Last Name (Required)'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control',
                                                               'placeholder': 'At least 8 characters.'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': "can't be entirely numeric."})
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_doctor', 'is_patient', 'first_name', 'last_name')


