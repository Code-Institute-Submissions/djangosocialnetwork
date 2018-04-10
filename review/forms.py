from django import forms
from .models import GameReview

class GameReviewForm(forms.ModelForm):
    class Meta:
        model=GameReview
        fields = ('title', 'content')