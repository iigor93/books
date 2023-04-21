from django.urls import path

from start_page.views import StartPageView

urlpatterns = [
    path("", StartPageView.as_view()),
]
