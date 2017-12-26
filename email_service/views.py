# from django.shortcuts import render
from django.http import HttpResponse
from email_service.logic import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def send(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data["user"]["user_id"]
        template = data["user"]["template"]
        user = query.create_user(user_id, template)
        mail = user.create_mail()
        return HttpResponse(sender.send_email(mail))
