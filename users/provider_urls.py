from django.urls import path
from .provider import ProviderSignup,ProviderSignin, ResendOTP

urlpatterns = [
    path('signup/',ProviderSignup.as_view(),name='provider_signup'),
    path('signin/',ProviderSignin.as_view(),name='provider_signin'),
    path('resend_otp/',ResendOTP.as_view(),name='resend_otp')
]