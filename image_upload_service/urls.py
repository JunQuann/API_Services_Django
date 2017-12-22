from django.conf.urls import url
from image_upload_service import views

urlpatterns = [
    url(r'^$', views.upload, name='upload')
]
