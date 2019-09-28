from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    gender = models.CharField(choices=CHOICES, max_length=6)
    started = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return self.full_name