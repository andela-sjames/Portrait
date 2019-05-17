import json

from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from webapp.utils.decorators import json_response
from webapp.forms import FacebookAuthForm

from webapp.models import SocialProfile



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
    def post(self, request, *args, **kwargs):
        """
        Logs a user out and redirects to the index view.
        """
        auth_form, token_expiry_time = FacebookAuthForm(request.POST)
        if auth_form.is_valid():
            # get or create the user:
            user = auth_form.save()
            if user:
                profile = user.social_profile
                profile.extra_data = json.dumps(request.POST)
                profile.save()
                # log the user in:
                login(request, user)
                self.request.session.set_expiry(token_expiry_time)
                # return success response:
                return {
                    'status': 'success',
                    'status_code': 200,
                    'loginRedirectURL': reverse('dashboard'),
                }
        # return error response
        return {'status': 'error', 'status_code': 403, }


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Represents the signed in users' dashboard/workspace view.
    """
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        context['profile'] = SocialProfile.objects.get(
            user=request.user)

        return self.render_to_response(context)
