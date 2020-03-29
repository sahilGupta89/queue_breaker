from django.urls import path, re_path
from .views import CategoryList,CategoryImage

urlpatterns = [
    path('service_list/',CategoryList.as_view(),name='services'),
    re_path(r'^uploads/catagories/(?P<filename>[-\w_\\-\\.]+)$', CategoryImage.as_view(), name='category_image-download'),
]