from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("userinput/", views.template, name='template'),
    path("userinput/userdata/", views.temp1, name='temp1'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about, name='about'),
]