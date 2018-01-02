from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from image_upload_service.logic import *
from django.http import HttpResponse

@csrf_exempt
def index(request):
    if request.method == 'POST':
        payload = parse(request)
        image_url = upload(image=payload['image_file'], key=payload['user_id'])
        return HttpResponse(put(image_url=image_url, auth_key=payload['auth_key'], user_id=payload['user_id']))
