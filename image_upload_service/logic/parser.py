def parse(request):
    user_id = request.POST['user_id']
    access_token = request.POST['access_token']
    image_file = request.FILES
    payload = {'user_id': user_id,
               'auth_key': auth_key,
               'image_file': image_file['image']}
    return payload
