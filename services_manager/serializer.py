from rest_framework import serializers
from .models import ProviderCategoryMapping, Categories

class ProviderCategoryMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCategoryMapping
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
