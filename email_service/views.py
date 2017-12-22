# from django.shortcuts import render
# from django.http import HttpResponse
from email_service.logic import *

# Create your views here.
def send(request, user_id, template):
    print(user_id)
    print(template)
    if request.method == "GET":
        user = query.create_user(user_id, template)
        to_send = user.create_mail()
        sender.send_email(to_send)
