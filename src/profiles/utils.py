import uuid

def slugid():
    id=str(uuid.uuid4())[:8].replace('_','').lower()
    return id