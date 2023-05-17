from rest_framework import viewsets

from book.models import Book
from book.serializers import BookSerializer


class BookListView(viewsets.ModelViewSet):
    """ Список книг """
    queryset = Book.objects.all()
    ic("dfff")
    serializer_class = BookSerializer
