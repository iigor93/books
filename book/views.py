from rest_framework import viewsets

from book.models import Book
from book.serializers import BookSerializer


class BookListView(viewsets.ModelViewSet):
    """ Список книг hello 5"""
    ic()
    queryset = Book.objects.all()
    serializer_class = BookSerializer
