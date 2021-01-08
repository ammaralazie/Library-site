from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,FileResponse,JsonResponse
from django.contrib.auth.models import User
from .models import *
import os
from project import settings
import json
from django.contrib import messages
from profiles.models import *
from django.contrib.auth.decorators import login_required
from .forms import EditBook,AddBook
history=[]
@login_required
def pdf_view(request,slug):
    
    obj2=Library.objects.get(slug=slug)
    if obj2 in history:
        print('history :','dont add')
    else:
        history.append(obj2)
        print('history :',history)
    lastredding(request,history)
    
    fs=os.path.join(settings.MEDIA_ROOT, str(obj2.content))
    if os.path.isfile(fs):
        response=HttpResponse(open(fs,'rb'),content_type='application/pdf')
        return response
    else:
        return HttpResponseNotFound('sorry this request is not valid')
@login_required
def reciveData(request):

    ####################
    body=json.loads(request.body)
    slug=body['slug']
    action=body['action']

    ###########################

    #############################
    book=Library.objects.get(slug=slug)
    profile=Profile.objects.get(name=request.user)
   ##############################
    if action == 'add':
        views=Views.objects.create(viewer=profile ,book_id=book.id)

        views.views_count+=1
        views.save()
    else:
        print('body: ',body)
    return JsonResponse('data has been recived',safe=False)
########################
@login_required
def filter_books(requset,str):
    message=''
    filter=Library.objects.getBooks(str)
    if filter:
        context={'obj':filter,'check':'True'}
        return render(requset,'index.html',context)
    else:
        message='We apologize, there is no book of this kind at this time. We suggest that you search for the name of the book from the search engine.'
        context={'x':message}
        return render(requset,'index.html',context)
####################################
@login_required
def search(request):
    try:
        if request.method=='GET':
            data=str(request.GET['search'])
            search=Library.objects.filter(book_name=data)
            if not search:
                search=Library.objects.filter(book_name=data.upper())
                
                if not search:
                    search=Library.objects.filter(book_name=data.lower())
                    if not search:
                        search=Library.objects.filter(book_name=data.replace('_',' ').upper())
                        
                        if not search:
                            search=Library.objects.filter(book_name=data.replace('_',' ').lower())
                            if not search:
                                search='There is no result'
                                return render(request,'search.html')

           
            return render(request,'search.html',{'search':search})
    except:
        pass

    #############################
@login_required
def create_commint(request):
    data=json.loads(request.body)

    slug=data['slug']
    print('slud :',slug)
    content=data['content']
    print('content :',content)

    user=Profile.objects.get(name=request.user)
    book=Library.objects.get(slug=slug)

    Commint.objects.create(user=user,book=book,content=content)
    
    return JsonResponse('data was submited',safe=False)


########################
@login_required
def delete_commint(requset):
    
    body=json.loads(requset.body)
    key=body['content']
    c=Commint.objects.get(id=key)
    c.delete()
    return JsonResponse('dataa was submited',safe=False)


@login_required
def addbook(request):
    profile=Profile.objects.get(name=request.user)
    if request.method =='POST':
        form=AddBook(request.POST,request.FILES)
        print('form: ',form)
        print('form: ',form.is_valid())
        if form.is_valid():
            print('form: ','is valid')
            instance=form.save(commit=False)
            instance.publisher=profile
            form.save()
            print('secusess')
            return redirect('profile:allBooks',profile.slug)

    else:
        form=AddBook()
        return render(request,'addbook.html',{'form':form})
def lastredding(request,history=history):
    if history:
        print('history :',history)
        return{'history':history}
    else:
        print('history :',history)
        return{'history':''}








    
    