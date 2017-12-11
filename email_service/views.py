# from django.shortcuts import render
# from django.http import HttpResponse
from email_service.logic import *

# Create your views here.
def send(request, user_id, template):
    user = query.create_user(user_id)
    to_send = user.create_mail()
    sender.send_async(to_send)
