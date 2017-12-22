# from django.shortcuts import render
# from django.http import HttpResponse
from email_service.logic import *

# Create your views here.
def send(request):
    if request.method == "POST":
        user_id = request.body["user"]
        template = request.body["template"]
        user = query.create_user(user_id, template)
        to_send = user.create_mail()
        sender.send_email(to_send)
