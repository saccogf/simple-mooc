from django.conf.urls import url
from simplemooc.accounts import views as accviews
from django.contrib.auth import views

urlpatterns = [
    url(r'^login/$', views.login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^register/$', accviews.register, name='register'),
    url(r'^logout/$', views.logout,
        {'next_page': 'core:home'}, name='logout'),
    url(r'^dashboard/$', accviews.dashboard, name='dashboard'),
    url(r'^edit/$', accviews.edit, name='edit'),
    url(r'^edit_password/$', accviews.edit_password, name='edit_password')
]
