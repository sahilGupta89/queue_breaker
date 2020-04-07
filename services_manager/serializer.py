from rest_framework import serializers
from .models import ProviderCategoryMapping, Categories, ProvidersTimeSlot,ConsumerTimeSlotMapping
from users.serializer import UserSerializer

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class ProviderCategoryMappingSerializer(serializers.ModelSerializer):
    # category = CategoriesSerializer(read_only=True)
    # provider = ProviderSerializer(read_only=True)
    # provider = serializers.SerializerMethodField()

    class Meta:
        model = ProviderCategoryMapping
        fields = ['provider', 'category', 'created', 'deleted', 'updated', 'id']


class ProvidersTimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvidersTimeSlot
        fields = "__all__"


class ConsumerTimeSlotMappingSerializer(serializers.ModelSerializer):
    consumer = UserSerializer()
    time_slot = ProvidersTimeSlotSerializer()

    class Meta:
        model = ConsumerTimeSlotMapping
        fields = "__all__"