from django.conf.urls import url
from email_service import views

urlpatterns = [
    url(r'^(?P<user_id>[\d+])/(?P<template>[\w]{4})', views.send, name='send'),
]
