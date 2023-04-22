from django.urls import path
from rest_framework.routers import DefaultRouter

from book.views import BookListView


books_list_ = BookListView.as_view({
    'get': 'list',
    'post': 'create'
})

book_detail = BookListView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', books_list_, name='books_list'),
    path('<int:pk>/', book_detail, name='book_detail'),
]
# router = DefaultRouter()
# router.register(r'', BookListView, basename='books_list')
# urlpatterns = router.urls
