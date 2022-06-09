from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):

        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        # self.username = UsernameField(widget=forms.TextInput(
        #     attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter username'}))
        # self.password1 = forms.CharField(widget=forms.PasswordInput(
        #     attrs={
        #         'class': 'form-control form-control-lg',
        #         'placeholder': 'Enter password'}))
        # self.password2 = forms.CharField(widget=forms.PasswordInput(
        #     attrs={
        #         'class': 'form-control form-control-lg',
        #         'placeholder': 'Enter password'}))






