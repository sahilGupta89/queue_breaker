from django.urls import path
from django.conf.urls import url
from .consumer import ConsumerSignup, ConsumerSignin,GenerateOTP
from .provider import ProviderSignup,ProviderSignin

urlpatterns = [
    path('signup/',ConsumerSignup.as_view(),name='signup'),
    path('signin/',ConsumerSignin.as_view(),name='signin'),
    path('generate_otp/',GenerateOTP.as_view(),name='generate_otp')
]