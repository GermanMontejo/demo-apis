from django.db import models


"""Book model for fetching and posting new book data"""
class Book(models.Model):
    title = models.CharField(max_length=256, default='', blank=True)
    author = models.CharField(max_length=128, default='', blank=True)
    date_pub = models.DateTimeField()
