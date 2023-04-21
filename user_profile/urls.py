from django.urls import path
from user_profile.views import UserProfileUpdateView

urlpatterns = [
    path("<int:pk>", UserProfileUpdateView.as_view()),
]
