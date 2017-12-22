from django.conf.urls import url
from email_service import views

urlpatterns = [
    url(r'^$', views.send, name='send'),
]
