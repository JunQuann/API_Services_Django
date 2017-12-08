from django.conf.urls import url
from email_service import views

urlpatterns = [
    url(r'^([\d]+)/([\w]{4})', views.send, name='send')
]
