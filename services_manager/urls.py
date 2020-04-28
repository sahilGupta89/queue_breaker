from django.urls import path, re_path
from django.conf.urls import url
from .views import CategoryList, CategoryImage, FetchProvidersByCategory, \
    FetchAvailableTimeSlot, UserAppVersion, UserNotifications
from django.views.generic import TemplateView


urlpatterns = [
    path('service_list/', CategoryList.as_view(), name='services'),
    path('available_time_slot/', FetchAvailableTimeSlot.as_view(), name='available_time_slot'),
    path('providers_by_categories/<int:category_id>/', FetchProvidersByCategory.as_view(),
         name='providers_by_categories'),
    re_path(r'^uploads/catagories/(?P<filename>[-\w_\\-\\.]+)$', CategoryImage.as_view(),
            name='category_image-download'),
    path('notification/', UserNotifications.as_view(), name='add_notification'),
    path('appversion/', UserAppVersion.as_view(), name='add_notification'),
    path('privacy_policy/',TemplateView.as_view(template_name='p'))
]
