from django import forms
from .models import *


class EditBook(forms.ModelForm):
    class Meta:
        model=Library
        fields=['book_name','Description','image']


class AddBook(forms.ModelForm):
    class Meta:
        model=Library
        fields=['book_name','Description','image','content','type_of_book']