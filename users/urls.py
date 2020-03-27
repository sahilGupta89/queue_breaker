from django.urls import path
from .views import ConsumerSignup, ConsumerSignin,GenerateOTP,VerifyOTP

urlpatterns = [
    path('signup/',ConsumerSignup.as_view(),name='signup'),
    path('signin/',ConsumerSignin.as_view(),name='signin'),
    path('generate_otp/',GenerateOTP.as_view(),name='generate_otp'),
    # path('verify_otp/',VerifyOTP.as_view(),name='verify_otp'),
]