import random
from .models import PhoneTokens
from .serializer import PhoneTokensSerializer


def verify_user_otp(phone, otp, user):
    if user and otp:
        try:
            phone_token_instance = PhoneTokens.objects.get(otp=otp, phone=user.phone)
            phone_token = PhoneTokensSerializer(phone_token_instance)
            if phone_token:
                serializer = PhoneTokensSerializer(instance=phone_token_instance, data={'is_verified': True})
                serializer.is_valid()
                serializer.save()
                return 'done'
        except Exception as e:
            return 'invalid_otp'
    else:
        return 'invalid_otp'


def generate_otp():
    otp = ""
    for i in range(4):
        otp += str(random.randint(1, 9))
    print("Your One Time Password is {}".format(otp))
    print(type(otp))
    return int(otp)


def send_otp(user):
    otp = generate_otp()
    if PhoneTokens.objects.filter(phone=user.phone).exists():
        # update
        serializer = PhoneTokensSerializer(PhoneTokens.objects.get(phone=user.phone),
                                           {'otp': otp, 'otp_sent': True, 'is_verified': False})
        serializer.is_valid()
        serializer.save()
        return serializer.data
    else:
        serializer = PhoneTokensSerializer(
            data={'otp': otp, 'phone': user.phone, 'otp_sent': True, 'is_verified': False})
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return None