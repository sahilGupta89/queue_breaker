from django.urls import path
from .provider import ProviderSignup,ProviderSignin, ResendOTP, GenerateOTP,UpdateServiceStatus,AddTimeSlot

urlpatterns = [
    path('signup/', ProviderSignup.as_view(), name='provider_signup'),
    path('signin/', ProviderSignin.as_view(), name='provider_signin'),
    path('resend_otp/', ResendOTP.as_view(), name='resend_otp'),
    path('generate_otp/', GenerateOTP.as_view(), name='generate_otp'),
    path('add_time_slot/', AddTimeSlot.as_view(), name='add_time_slot'),
    path('update_service_status/', UpdateServiceStatus.as_view(), name='update_service_status'),
]