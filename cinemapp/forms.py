from django import forms
from .models import Film
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class FilmForm(forms.ModelForm):
    hours = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Enter hours separated by comma'
                                }
                            ))

    class Meta:
        model = Film
        fields = ['title', 'genre', 'type', 'duration', 'hours', 'image']

    def clean_hours(self):
        hours = self.cleaned_data.get('hours')
        return [hour.strip() for hour in hours.split(',')] if hours else []

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=UserProfile.ROLE_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adaugă clase CSS pentru styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Creează profilul utilizatorului cu rolul ales
            UserProfile.objects.create(
                user=user,
                role=self.cleaned_data['role']
            )
        return user