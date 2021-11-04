from . import template_credentials
ID = 'template'

creds = template_credentials.creds

def send(dest,msg,additional_info=None):
    print('sending message:\n',msg,'\nto',dest,'with credentials:\n',creds)
    success = True
    if success:
        return True
