from django.urls import path
from collaborators import views


urlpatterns = [
    path('collaborators/', views.CollaboratorList.as_view()),
    path('collaborators/<int:pk>', views.CollaboratorDetail.as_view()),
]