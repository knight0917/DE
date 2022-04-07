from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),    

    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),

    path("userinput/", views.template, name='template'),
    path("userinput/userdata/", views.temp1, name='temp1'),
    path("about/", views.about, name='about'),
]