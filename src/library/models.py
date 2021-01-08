from django.db import models
from profiles.models import Profile
import datetime
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from .utils import slugid
from profiles.models import Profile 
# Create your models here.

class filterData(models.Manager):
    def getBooks(requset,data):
        obj=Library.objects.filter(type_of_book=data)
        return obj






class Library(models.Model):
    publisher=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='publisher')
    book_name=models.CharField(max_length=100)
    published=models.DateField(default=datetime.datetime.now)
    Description=models.TextField()
    image=models.ImageField(upload_to='library')
    content=models.FileField(FileExtensionValidator(['pdf']))
    slug=models.SlugField(blank=True)

    TUPE_OF_BOOK=(('realistic','realistic'),('Imaginary','Imaginary'),('Science Fiction','Science Fiction'),('Drama','Drama'),('Adventure, and excitement','Adventure, and excitement'),('Romance','Romance'),('Ambiguity','Ambiguity'),('Horror','Horror'),('the health','the health'),('Travel','Travel'),('Children book','Children book'),('Guide','Guide'),('Religious and spiritual book','Religious and spiritual book'),('the scientific book','the scientific book'),('Historical','Historical'),('Mathematics','Mathematics'),('Encyclopedias','Encyclopedias'),('the dictionary','the dictionary'),('Short stories','Short stories'),('the art','the art'),('Cookbooks','Cookbooks'),('Notes','Notes'))

    type_of_book=models.CharField(max_length=40, choices=TUPE_OF_BOOK)
    objects=filterData()
    def __str__(self):
        return str(self.book_name)

    def save(self,*args,**kwargs):
        if self.slug=='':
            self.slug=slugify(slugid)
        super(Library,self).save(*args,**kwargs)
    def all_views(self):
        return self.views_set.all().count()

    def number_commint(self):
        all=self.commint_set.all().count()
        return all

    def all_commint(self):
        all=self.commint_set.all()
        return all


class Views(models.Model):
    viewer=models.ForeignKey(Profile,on_delete=models.CASCADE,verbose_name='The Viewer',related_name='viwer')
    book=models.ForeignKey(Library,on_delete=models.CASCADE,verbose_name='Book')
    views_count=models.IntegerField(default=0,blank=True)
    Views_time=models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return str(self.viewer)+str(self.book)+str(self.Views_time)


class Commint(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    book=models.ForeignKey(Library,on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    created=models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.user)+str(self.book)+str(self.created)