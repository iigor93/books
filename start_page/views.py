from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from book.models import Book


class StartPageView(View):

    template_name = "start_page/start_page.html"

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        context = {"welcome": "!welcome",
                   "books": books,
                   }
        return render(request, self.template_name, context)
