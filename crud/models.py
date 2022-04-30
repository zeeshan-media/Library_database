from django.db import models

# Create your models here.

class Crud(models.Model):
    name=models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    edition = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    book_id=models.IntegerField(max_length=30, primary_key=True)
    isbn=models.CharField(max_length=30)

