from django.db import models
from django.contrib.auth.models import User

class Film(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    hours = models.JSONField(default=list)
    image = models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('client', 'Client'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"

