from django import forms
from .models import Crud

class Book(forms.ModelForm):
    book_id= forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    edition = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    isbn = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    genre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model=Crud
        fields=['book_id','name','author','edition','isbn','genre']

