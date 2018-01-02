import os
import sendgrid
import urllib
from sendgrid.helpers.mail import Email, Content, Substitution, Mail

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get("SENDGRID_API_KEY"))

def send_email(email):
    try:
        response = sg.client.mail.send.post(request_body=email.get())
        return response.status_code
    except urllib.error.HTTPError as e:
        e.read()
