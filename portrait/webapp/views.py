from django.shortcuts import render
from django.views.generic import TemplateView, View

from utils.decorators import json_response


class LoginRequiredMixin(object):
    """
    View mixin which requires that the user is authenticated.
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class JsonResponseMixin(object):
    """
    View mixin which ensures a json response object is returned.
    """
    @method_decorator(json_response)
    def dispatch(self, request, *args, **kwargs):
        return super(JsonResponseMixin, self).dispatch(
            request, *args, **kwargs)


class HomeView(TemplateView):
    """Homepage View defined here."""

    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


class FacebookAuthView(JsonResponseMixin, View):
    """
    Logs a user in with their facebook account.
    """
    pass