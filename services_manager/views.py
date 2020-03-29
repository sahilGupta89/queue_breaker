import random
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse,HttpResponse
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import CategoriesSerializer, ProviderCategoryMappingSerializer
from .models import Categories
from django.conf import settings

class CategoryList(APIView):
    serializer_class = CategoriesSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, ]

    def get(self, request):
        try:
            base_url = "http://localhost:8000/api"
            serializer = CategoriesSerializer(data=Categories.objects.all(), many=True)
            serializer.is_valid()
            for category in serializer.data:
                category['image'] = base_url+category['image']
            return Response(data={'msg': "Retrived data", 'success': True, 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'msg': "Categories not found", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)


class CategoryImage(APIView):
    serializer_class = CategoriesSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, ]

    def get(self, request, *args, **kwargs):
        try:
            filename = self.kwargs.get('filename', None)
            if filename is None:
                raise ValueError("Found empty filename")
            some_file = Categories.objects.get(image="catagories/"+filename)
            response = FileResponse(some_file.image, content_type="image/file")
            response['Content-Disposition'] = 'attachment; filename="%s"' % filename
            return response
        except Exception as e:
            return Response(data={'msg': "File not found", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)