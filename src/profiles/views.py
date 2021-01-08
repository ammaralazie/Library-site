from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from library.models import Library
from .forms import EditProfile
from library.forms import EditBook
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.core.mail import send_mail

@login_required
def profile_view(request,slug):
    obj=Profile.objects.get(slug=slug)
    return render(request,'sss.html',{'obj':obj})

def allBooks(request,slug):
    profile=Profile.objects.get(slug=slug)
    all=Library.objects.filter(publisher=profile)
    return render(request,'allBook.html',{'obj':all})

#_________________________________________________#
@login_required
def editprofile(request,slug):
    profile=Profile.objects.get(slug=slug)
    autin=Profile.objects.get(name=request.user)
    if profile ==autin:
        if request.method =='POST':
            form=EditProfile(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.name=request.user
                instance.save()
                return redirect('profile:profile_view',slug)
        else:
            form=EditProfile(instance=profile)
            return render(request,'editprofile.html',{'form':form})
    else :
        return HttpResponse('ماكو هيج كلاوات ترة ')

#____________________________#
@login_required
def editbookforms(request,slug):
    
    book=Library.objects.get(slug=slug)
    profile=Profile.objects.get(name=request.user)
    if request.method =='POST':
        form=EditBook(request.POST ,request.FILES,instance=book)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.publisher=profile
            form.save()
            return redirect('profile:allBooks',profile.slug)
    else:
        form=EditBook(instance=book)
        return render(request,'editBook.html',{
          'form':form,
          
        })
@login_required
def deleteBook(request,slug):
    book=Library.objects.get(slug=slug)
    uuser=Profile.objects.get(name=request.user)
    if book.publisher == uuser:
        book.delete()
        return redirect('profile:allBooks',book.publisher.slug)
    else:
        return HttpResponse('اكعد راحة عمو لا تلعب  ')

def signup(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            form.save()
            user=authenticate(username=username,password=password)
            login(request,user) 
            new_user=User.objects.all()
            getUser=User.objects.get(pk=len(new_user))
            getProfile=Profile.objects.get(name=getUser)
            return redirect('profile:profile_view',getProfile.slug)
    else:
        form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})

def sendmessage(request):
    send_mail(
    'the subject',
    'the content of message',
    #the sender 
    'alaziiammar10@gmail.com',
    #the reciver
    ['alaziiammar@gmail.com'],
    fail_silently=False
    )
    return render(request,'email_sended.html')



