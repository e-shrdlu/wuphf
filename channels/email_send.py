from . import email_credentials
import smtplib

ID = 'email_send'
creds = email_credentials.creds

def send(dest,msg,additional_info=None):
    conn = smtplib.SMTP('smtp.gmail.com',587)
    conn.ehlo()
    conn.starttls()
    conn.login(creds['user'],creds['pass'])
    resp = conn.sendmail(creds['user'],dest,msg)
    if len(resp) == 0:
        return True
