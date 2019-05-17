from django.db import models
from django.contrib.auth.models import User


class SocialProfile(models.Model):
    """
    Represents information about a user
    authenticated via social media.
    """
    FACEBOOK = '1'
    PROVIDERS = (
        (FACEBOOK, 'Facebook'),
    )

    provider = models.SmallIntegerField(choices=PROVIDERS)
    social_id = models.CharField(max_length=255, unique=True)
    photo = models.TextField(blank=True)
    extra_data = models.TextField(blank=True)
    user_access_token = models.TextField(blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='social_profile')

    def __repr__(self):
        return f"{self.provider}:{self.social_id}"

    def __str__(self):
        return f"{self.provider}:{self.social_id}"
