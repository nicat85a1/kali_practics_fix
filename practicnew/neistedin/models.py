from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="userprofile")

    def __str__(self) -> str:
        return self.user.username

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length=100)
    explanation = models.TextField()
    tag = models.ManyToManyField(Tag)