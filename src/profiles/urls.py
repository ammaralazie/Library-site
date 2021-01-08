from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name='profiles'
urlpatterns = [
    path('<slug:slug>',profile_view,name='profile_view'),
    path('<slug:slug>/allBooks',allBooks,name='allBooks'),
    path('<slug:slug>/editprofile',editprofile,name='editprofile'),
    path('<slug:slug>/edit_book/',editbookforms,name='editbookforms'),
    path('<slug:slug>/delet_Book/',deleteBook,name='deleteBook'),
    path('SignUp/',signup,name='signup'),
    path('sendmessage/',sendmessage,name='sendmessage'),

   


    
    
    
    
]