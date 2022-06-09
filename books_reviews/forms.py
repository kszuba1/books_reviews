from django import forms
from .models import Review
from django.contrib.auth.forms import AuthenticationForm, UsernameField


#  review form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'book_title', 'book_author', 'description', 'rate')

        rate_choices = (
            (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
            (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'),
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter review title...'}),
            'book_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title...'}),
            'book_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book author...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5,
                                                 'placeholder': 'Enter description...'}),
            'rate': forms.Select(attrs={'class': 'form-control'}, choices=rate_choices),
        }


#  custom login form
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter password'}))
