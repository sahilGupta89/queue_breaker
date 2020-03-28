from django.urls import path
from .views import CategoryList

urlpatterns = [
    path('service_list/',CategoryList.as_view(),name='services')
]