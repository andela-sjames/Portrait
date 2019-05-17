from django import forms
from django.contrib.auth.models import User

from webapp.models import SocialProfile

class FacebookAuthForm(forms.Form):
    """
    Form for validating and saving Facebook
    user authentication data. Returns the
    existing or created user.
    """

    id = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    photo = forms.CharField(required=False)

    def save(self):
        """
        gets returns the social user with the form data.
        creates one if it does not already exists.
        """
        data = self.cleaned_data
        user = None
        try:
            # get associated user if it exists:
            social_id = data['id']
            social_profile = SocialProfile.objects.get(
                provider=SocialProfile.FACEBOOK,
                social_id=social_id,
            )
            user = social_profile.user

        except SocialProfile.DoesNotExist:
            # Create the user:
            user = User(
                username=data['id'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            user.save()

            # make call to graphAPI to get long-lived access token

            # Create the user's social_profile:
            social_profile = SocialProfile(
                provider=SocialProfile.FACEBOOK,
                social_id=data['id'],
                photo=data['photo'],
                user=user
            )
            social_profile.save()

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        return user
