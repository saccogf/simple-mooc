from django.conf.urls import url
from simplemooc.accounts import views as accviews
from django.contrib.auth import views

urlpatterns = [
    url(r'^login/$', views.login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^register/$', accviews.register,
        {'template_name': 'accounts/register.html'}, name='register'),
]
