from django.conf.urls.defaults import *
from django.conf import settings
from views import *


urlpatterns = patterns('', 
    url(r'^contactus/$', contactus.as_view(), name='contactus'),
    url(r'^contactus/thankyou/$', thankyou.as_view(), name='thankyou'),
)
