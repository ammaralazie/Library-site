from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save,sender=User)
def createprofile(sender,instance,created,**kwargs):
    print('instance :',instance)
    if created :
        name=instance
        Profile.objects.create(name=name)

