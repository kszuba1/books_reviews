
from django import forms
from django.forms import ModelForm
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

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
            'user': forms.Select(attrs={'class': 'form-control'}),
        }


