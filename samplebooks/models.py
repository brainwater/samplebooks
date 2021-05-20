from django.db import models

# Create your models here.

class Book(models.Model):
    google_volume_id = models.CharField(max_length=128, unique=True, primary_key=True)

class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

