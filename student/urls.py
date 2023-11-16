from django.urls import path

from . import views

app_name = "student"
urlpatterns = [
    path('', views.student_home, name="student_home"),
    path('practice', views.practice_entry, name="practice_entry"),
    path('practice-history', views.practice_history, name="practice_history"),
]