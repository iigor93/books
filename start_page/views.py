from django.views.generic import TemplateView


class StartPageView(TemplateView):
    template_name = "start_page/start_page.html"
