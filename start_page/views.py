from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class StartPageView(View):

    template_name = "start_page/start_page.html"

    def get(self, request, *args, **kwargs):
        context = {"welcome": "!welcome"}
        return render(request, self.template_name, context)
