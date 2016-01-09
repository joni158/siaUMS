from django import forms
from django.contrib.auth.models import User

from .models import Mahasiswa

class Mahasiswa(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')