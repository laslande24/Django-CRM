from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter your email address"
    }
    ))
    first_name = forms.CharField(label="First name", max_length="100", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter your first name"
    }
    ))
    last_name = forms.CharField(label="Last name", max_length="100", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter your last name"
    }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        self.field

