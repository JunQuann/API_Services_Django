import os
import sendgrid

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get("SENDGRID_API_KEY"))

def send_email(email):
    try:
        response = sg.client.mail.send.post(request_body=email.get())
    except urllib.error.HTTPError as e:
        e.read()
