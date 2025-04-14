from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    hours = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Enter hours separated by comma'
                                }
                            ))

    class Meta:
        model = Film
        fields = ['title', 'genre', 'type', 'duration', 'hours']

    def clean_hours(self):
        hours = self.cleaned_data.get('hours')
        return [hour.strip() for hour in hours.split(',')] if hours else []