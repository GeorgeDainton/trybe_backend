from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.GoalAPIView.as_view()),
    path("goals/", views.GoalAPIView.as_view()),
    path("goals/<int:id>/", views.GoalDetailAPIView.as_view()),
    path("goals/<int:id>/messages/", views.MessagesAPIView.as_view()), 
    path("supporters/add/", views.InvitedSupporterAPIView.as_view()),
    path("supporters/connect/", views.AcceptedSupporterAPIView.as_view()),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
]
