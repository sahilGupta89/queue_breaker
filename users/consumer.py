import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, Token
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, PhoneTokens, Location
from services_manager.models import ConsumerTimeSlotMapping
from services_manager.serializer import ConsumerTimeSlotMappingSerializer, ConsumerTimeSlotMappingRelationSerializer
from .serializer import UserSerializer, PhoneTokensSerializer, UserPhoneSerializer,LocationSerializer
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


# check user in db if not create
class GenerateOTP(APIView):
    serializer_class = PhoneTokensSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, ]

    def post(self, request):
        try:
            phone = request.data['phone']
            user = get_queryset(phone)
            if user and phone:
                # send OTP to user
                user = get_queryset(phone)
                otp_status = send_otp(user)
                return Response({'data': otp_status, 'success': True, 'msg': 'OTP sent'}, status=status.HTTP_200_OK)
            elif phone:
                # create user
                new_user = UserPhoneSerializer(data={'phone': phone})
                new_user.is_valid()
                new_user.save()
                # send otp
                otp_status = send_otp(get_queryset(phone))
                return Response({'data': otp_status, 'success': True, 'msg': 'OTP sent'}, status=status.HTTP_200_OK)
            else:
                return Response({'msg': 'Please provide phone number', 'success': False, 'data': ''},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': e.args, 'success': False, 'data': ''}, status=status.HTTP_404_NOT_FOUND)


class VerifyOTP(APIView):
    serializer_class = PhoneTokensSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, ]

    def post(self, request):
        try:
            phone = request.data['phone']
            otp = request.data['otp']
            verification_status = verify_user_otp(phone, otp, get_queryset(phone))
            if verification_status == 'done':
                return Response({'msg': 'Verification done'}, status=status.HTTP_200_OK)
            else:
                return Response(data={'msg': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={'msg': e.args}, status=status.HTTP_404_NOT_FOUND)


class ConsumerSignup(APIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, MultiPartParser]

    def post(self, request, format=None):
        if not User.objects.filter(phone=request.data['phone']).exists():
            if "password" in request.data:
                request.data['password'] = make_password(request.data['password'])
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    serializer.save()
                    location_serializer = LocationSerializer(data={"user":serializer.data['id']})
                    location_serializer.is_valid(raise_exception=True)
                    location_serializer.save()
                except Exception as e:
                    return Response(data={'msg': e.args, 'success': False, 'data': ''},
                                    status=status.HTTP_208_ALREADY_REPORTED)
            else:
                return Response(data={'msg': "Please provide valid parameters", 'success': False, 'data': ''},
                                status=status.HTTP_400_BAD_REQUEST)
            return Response(data={'data': serializer.data, 'success': True, 'msg': 'Data saved'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data={'msg': "Already registered", 'success': False, 'data': ''},
                            status=status.HTTP_208_ALREADY_REPORTED)


class ConsumerSignin(APIView):
    pass
    serializer_class = UserSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, ]

    def post(self, request):
        # authenticate(request,email=request.data['phone'],password=request.data['password'])
        try:
            user = UserSerializer(get_queryset(request.data['phone']))
            if user:
                # Verify otp
                phone = request.data['phone']
                otp = request.data['otp']
                verification_status = verify_user_otp(phone, int(otp), get_queryset(phone))

                if verification_status == 'done':
                    data_to_send = dict()
                    data_to_send.update({"user": user.data})
                    data_to_send['user'].update({
                        "verification_status": verification_status,
                        "location": LocationSerializer(Location.objects.get(user=user.data['id'])).data
                    })

                    new_token = RefreshToken.for_user(get_queryset(phone))
                    data_to_send.update({
                        'refresh_token': str(new_token),
                        'access_token': str(new_token.access_token),
                    })
                    return Response({'msg': 'Verification done', 'success': True, 'data': data_to_send},
                                    status=status.HTTP_200_OK)
                else:
                    return Response(data={'msg': 'User not found', 'success': False, 'data': ''},
                                    status=status.HTTP_404_NOT_FOUND)

                # if "password" in request.data and user.check_password(request.data['password']):
                #     serializer = UserSerializer(user)
                # else:
                #     return Response({'msg': 'Check your password', 'data': []}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'msg': 'User not found', 'success': False, 'data': ''},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': e.args, 'success': False, 'data': ''}, status=status.HTTP_404_NOT_FOUND)


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


class BookTimeSlot(APIView):
    permission_classes = ([AllowAny])

    def post(self, request):
        try:
            consumer_id = None if "consumer_id" not in request.data else request.data['consumer_id']
            time_slot_id = None if "time_slot_id" not in request.data else request.data['time_slot_id']
            data_to_save = dict()
            data_to_save.update({
                "consumer": consumer_id,
                "time_slot": time_slot_id
            })
            serializer = ConsumerTimeSlotMappingSerializer(data=data_to_save)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data={'msg': "Booking done", 'success': True, 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'msg': "Please Provide valid data", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)


class FetchBooking(APIView):
    permission_classes = ([AllowAny])

    def get(self, request):
        try:
            consumer_id = request.query_params['consumer_id']
            # phone = None if "phone" not in request.query_params else request.query_params['phone']
            queryset = ConsumerTimeSlotMapping.objects.select_related('time_slot','consumer').filter(consumer__id__contains=consumer_id)
            serializer = ConsumerTimeSlotMappingRelationSerializer(queryset, many=True)
            # user_detail = get_queryset(phone)

            return Response(data={'msg': "Retrieved  data", 'success': True, 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'msg': "Data not found", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)
