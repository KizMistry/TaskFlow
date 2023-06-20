from django.urls import path
from profiles import views

urlpatterns = [
    paths('/profiles', views.ProfileList.as_view()),
]