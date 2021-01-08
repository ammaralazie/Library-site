from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .utils import slugid
import datetime
class Profile(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='name')
    first_name=models.CharField(max_length=20, null=True ,blank=True)
    last_name=models.CharField(max_length=20, null=True ,blank=True)
    avatar=models.ImageField(upload_to='media')
    created=models.DateTimeField(default=datetime.datetime.now)
    describtion=models.TextField(blank=True)
    slug=models.SlugField(blank=True)


    def __str__(self):
        return str(self.name)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(slugid)
        super(Profile,self).save(*args,**kwargs)

    def num_book(self):
        return self.publisher.all().count()
            




