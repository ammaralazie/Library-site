import uuid
def slugid(request):
    s=str(uuid.uuid4())[:8].replace('_','').lower()
    return s