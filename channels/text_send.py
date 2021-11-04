from . import email_send

ID = 'text_send'

def send(dest,msg,additional_info=None): # additional_info is carrier email. should be of form "{}@carrieremail.com", where {} is where a phone number would go. use https://email2sms.info/ to find email
    return email_send.send(additional_info.format(dest),msg) #  send email to carrier email, ex: 1235554567@vtext.com (verizon)
