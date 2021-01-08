from django.urls import path
from .views import *
app_name='library'

urlpatterns=[
    path('<slug:slug>',pdf_view,name='pdf_view'),
    path('reciveData/',reciveData,name='reciveData'),
    path('filter_books/<str:str>',filter_books,name='filter_books'),
    path('search/',search,name='search'),
    path('create_commint/',create_commint,name='create_commint'),
    path('delete_commint/',delete_commint,name='delete_commint'),
    path('add_book/',addbook,name='addbook'),

]
