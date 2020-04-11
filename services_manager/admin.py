from django.contrib import admin
from .models import ProviderCategoryMapping,Categories,ConsumerTimeSlotMapping, ProvidersTimeSlot, AppVersion, Notifications

# Register your models here.

admin.site.register(ProviderCategoryMapping)
admin.site.register(Categories)
admin.site.register(ConsumerTimeSlotMapping)
admin.site.register(ProvidersTimeSlot)
admin.site.register(Notifications)
admin.site.register(AppVersion)