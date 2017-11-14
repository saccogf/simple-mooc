from django.conf.urls import url
from simplemooc.core import views  # Imports from INSTALLED_APPS in settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
]
