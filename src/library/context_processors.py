from profiles.models import Profile

def nav(requset):
    print(requset.user.is_authenticated)
    if requset.user.is_authenticated:
        objects=Profile.objects.get(name=requset.user)
    else:
        objects='Login'
    return{'objects':objects}