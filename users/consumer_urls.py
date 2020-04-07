from django.urls import path, re_path
from .consumer import ConsumerSignup, ConsumerSignin, GenerateOTP, ResendOTP, BookTimeSlot, FetchBooking

urlpatterns = [
    path('signup/', ConsumerSignup.as_view(), name='signup'),
    path('signin/', ConsumerSignin.as_view(), name='signin'),
    path('generate_otp/', GenerateOTP.as_view(), name='generate_otp'),
    path('resend_otp/', ResendOTP.as_view(), name='resend_otp'),
    path('book_time_slot/', BookTimeSlot.as_view(), name='book_time_slot'),
    path('fetch_booking/', FetchBooking.as_view(), name='fetch_booking'),
]
