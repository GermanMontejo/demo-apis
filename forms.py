from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'date_pub']
        labels = {'title': 'title', 'author': 'author', 'date_pub': 'date_pub'}
