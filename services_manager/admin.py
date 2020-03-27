from django.contrib import admin
from .models import ProviderCategoryMapping,Categories,ConsumerTimeSlotMapping, ProvidersTimeSlot
# Register your models here.

admin.site.register(ProviderCategoryMapping)
admin.site.register(Categories)
admin.site.register(ConsumerTimeSlotMapping)
admin.site.register(ProvidersTimeSlot)