import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, PhoneTokens
from .serializer import UserSerializer, UserPhoneSerializer, ProviderSerializer
from .utils import send_otp, verify_user_otp


def get_queryset(phone):
    """
    This view should return a list of all authenticated user.
    """
    # user = self.request.user
    if User.objects.filter(phone=phone).exists():
        return User.objects.get(phone=phone)
    else:
        return None


class ProviderSignup(APIView):
    # name,email,phone,categorytype
    serializer_class = UserSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, MultiPartParser]

    def post(self, request):
        if not User.objects.filter(phone=request.data['phone']).exists():
            if "password" in request.data:
                request.data['password'] = make_password(request.data['password'])
            if "address" in request.data:
                # create location
                location = 3
                provider_data = {
                    'first_name': request.data.first_name,
                    'email': request.data.email,
                    'phone': request.data.phone,
                    'roles': request.data.roles,
                    'location': location
                }
                serializer = ProviderSerializer(data=provider_data)
            else:
                serializer = UserPhoneSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    serializer.save()
                    # send otp
                    otp_status = send_otp(get_queryset(request.data['phone']))
                except Exception as e:
                    return Response(data={'msg': e.args, 'success': False, 'data': ''},
                                    status=status.HTTP_208_ALREADY_REPORTED)
                return Response({'data': otp_status, 'success': True, 'msg': 'OTP sent'}, status=status.HTTP_200_OK)
            else:
                return Response(data={'msg': "Please provide valid parameters", 'success': False, 'data': ''},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'msg': "Already registered", 'success': False, 'data': ''},
                            status=status.HTTP_208_ALREADY_REPORTED)


class ResendOTP(APIView):
    # name,email,phone,categorytype
    serializer_class = UserSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser]

    def post(self, request):
        try:
            phone = request.data['phone']
            otp_status = send_otp(get_queryset(phone))
            return Response(data={'msg': "OTP sent", 'success': True, 'data': otp_status},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'msg': "Please Provide valid phone number", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)


# verfy otp and send signin info
class ProviderSignin(APIView):
    serializer_class = UserSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser]

    def post(self, request):
        try:
            phone = request.data['phone']
            otp = request.data['otp']
            phone = request.data['phone']
            verification_status = verify_user_otp(phone, otp, get_queryset(phone))
            if verification_status =="done":
                return Response(data={'msg': "Successfully signed in", 'success': True, 'data': verification_status},
                                status=status.HTTP_200_OK)
            else:
                return Response(data={'msg': "Invalid OTP", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(data={'msg': e.args, 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)
