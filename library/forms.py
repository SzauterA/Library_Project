from django import forms
from .models import Book, Author

class BookForm(forms.Form):  
    title = forms.CharField(max_length=100, required=False)
    

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
   