from django.urls import re_path

from webapp import views

urlpatterns = [
    re_path(r'^$', 
        views.HomeView.as_view(), 
        name="homepage"),

    re_path(r'^auth/facebook/$',
        views.FacebookAuthView.as_view(),
        name='facebook_auth'),
]
