from rest_framework import serializers
# from django.contrib.auth.models import User, Group
from .models import User, PhoneTokens, AccessTokens


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        # fields = ['image', 'email', 'phone', 'first_name', 'last_name','password']
        fields = ['first_name', 'email', 'phone']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','email','phone','location','roles']


class UserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone']


class PhoneTokensSerializer(serializers.ModelSerializer):
    # user = ConsumerSerializer(allow_null=True)
    class Meta:
        model = PhoneTokens
        fields = ['phone', 'otp_sent', 'otp', 'is_verified']
