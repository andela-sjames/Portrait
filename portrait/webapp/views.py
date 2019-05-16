from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Homepage View defined here."""

    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)
