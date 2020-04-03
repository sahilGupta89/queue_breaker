from rest_framework import serializers
from .models import ProviderCategoryMapping, Categories, ProvidersTimeSlot
from users.serializer import ProviderSerializer


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
