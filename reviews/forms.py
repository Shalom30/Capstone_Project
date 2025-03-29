# reviews/forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie_title', 'review_content', 'rating']
        widgets = {
            'movie_title': forms.TextInput(attrs={'class': 'form-control'}),
            'review_content': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }