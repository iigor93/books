from django.urls import path
from rest_framework.routers import DefaultRouter

from book.views import BookListView


router = DefaultRouter()
router.register(r'', BookListView, basename='books_list')
urlpatterns = router.urls
