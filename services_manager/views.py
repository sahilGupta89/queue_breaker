import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import CategoriesSerializer, ProviderCategoryMappingSerializer
from .models import Categories


class CategoryList(APIView):
    serializer_class = CategoriesSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, ]

    def get(self, request):
        try:
            serializer = CategoriesSerializer(data=Categories.objects.all(), many=True)
            serializer.is_valid()
            return Response(data={'msg': "Retrived data", 'success': True, 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'msg': "Categories not found", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)
