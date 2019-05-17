from django.urls import re_path

from webapp import views

urlpatterns = [
    re_path(r'^$', 
        views.HomeView.as_view(), 
        name="homepage"),

    re_path(r'^auth/facebook/$',
        views.FacebookAuthView.as_view(),
        name='facebook_auth'),

    re_path(r'^dashboard/$',
        views.DashboardView.as_view(),
        name='dashboard'),

    re_path(r'^logout/$',
        views.LogOutView.as_view(),
        name='logout'),
]
