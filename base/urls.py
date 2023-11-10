from django.urls import path

from . import views

app_name = "base"

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),
]