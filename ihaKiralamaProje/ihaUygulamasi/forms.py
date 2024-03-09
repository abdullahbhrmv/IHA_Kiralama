# ihaUygulamasi/forms.py

from django import forms
from .models import IHA, Kiralama
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class IHAForm(forms.ModelForm):
    class Meta:
        model = IHA
        fields = '__all__'

class KiralamaForm(forms.ModelForm):
    class Meta:
        model = Kiralama
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    phone_number = forms.CharField(max_length=15, required=True, help_text='Required. Enter a valid phone number.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')
