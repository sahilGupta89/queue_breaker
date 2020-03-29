from django.urls import path,re_path
from .consumer import ConsumerSignup, ConsumerSignin,GenerateOTP,ResendOTP

urlpatterns = [
    path('signup/',ConsumerSignup.as_view(),name='signup'),
    path('signin/',ConsumerSignin.as_view(),name='signin'),
    path('generate_otp/',GenerateOTP.as_view(),name='generate_otp'),
    path('resend_otp/',GenerateOTP.as_view(),name='resend_otp')
]