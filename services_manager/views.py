import random
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse,HttpResponse
from rest_framework import status,serializers
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import CategoriesSerializer, ProviderCategoryMappingSerializer
from users.serializer import UserSerializer,LocationSerializer
from .models import Categories,ProviderCategoryMapping,ProvidersTimeSlot,ConsumerTimeSlotMapping
from users.models import User
from common_utils import distance

base_url = "http://35.223.14.120:8000/api"

def get_queryset(role,phone,user_id):
    if user_id and role:
        return UserSerializer(id=user_id,roles=role)
    if role and phone:
        return UserSerializer(phone=phone,roles=role)


class CategoryList(APIView):
    serializer_class = CategoriesSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, ]

    def get(self, request):
        try:
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


class FetchProvidersByCategory(APIView):
    # distance('53.32055555555556','-1.7297222222222221','53.32055555555556','-1.6997222222222223')
    serializer_class = ProviderCategoryMappingSerializer
    permission_classes = ([AllowAny])
    parser_classes = [JSONParser, ]
    def get(self,request,**kwargs):
        try:
            # fetch provider with categories
            category_id = kwargs['category_id']

            queryset = User.objects.filter(providercategorymapping__category__id=category_id)
            if len(queryset)!=0:
                data_to_send= dict()
                _category = queryset[0].providercategorymapping_set.filter(category_id=category_id)
                if len(_category)!= 0:
                    _catetory_serializer = CategoriesSerializer(_category[0].category)
                    data_to_send.update({'category':_catetory_serializer.data})
                    data_to_send['category'].update({
                        'image': base_url + data_to_send['category']['image']
                    })
                    data_to_send.update({'providers':[]})

                    for d in queryset:
                        provider_dict = dict()
                        provider_dict.update(UserSerializer(d).data)
                        provider_dict.update({'location':LocationSerializer(d.location_set.all()[0]).data})
                        data_to_send['providers'].append(provider_dict)

                    return Response(data={'msg': "Retrived data", 'success': True, 'data': data_to_send},
                                    status=status.HTTP_200_OK)
                else:
                    return Response(data={'msg': "Category not found", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data={'msg': "User not found", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print('error>>>>>>>>>',e.args)
            return Response(data={'msg': "Data not found", 'success': False, 'data': ''},
                            status=status.HTTP_404_NOT_FOUND)
