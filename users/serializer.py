from rest_framework import serializers
# from django.contrib.auth.models import User, Group
from .models import User, PhoneTokens, AccessTokens, Location


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        # fields = ['image', 'email', 'phone', 'first_name', 'last_name','password']
        fields = ['first_name', 'email', 'phone','id']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'phone', 'roles', 'id','is_active']


class UserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone','id']


class PhoneTokensSerializer(serializers.ModelSerializer):
    # user = ConsumerSerializer(allow_null=True)
    class Meta:
        model = PhoneTokens
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
