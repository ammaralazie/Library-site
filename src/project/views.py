from django.shortcuts import render
from django.http import JsonResponse
from library.models import Library
from django.core.paginator import Paginator
def home(requset):
    obj=Library.objects.all()
    paginator=Paginator(obj,8)
    print(requset.GET)
    page_number=requset.GET.get('page')
    obj=paginator.get_page(page_number)
    return render(requset,'base.html',{'obj':obj})
