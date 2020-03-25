from django.contrib.gis.db import models
from users.models import User
# Create your models here.


class Categories:
    name = models.CharField(max_length=50,blank=False,null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)


class ProvidersTimeSlot:
    provider = models.ForeignKey(User,on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='service start time')
    end_time = models.DateTimeField(verbose_name='service end time')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)


class ProviderCategoryMapping:
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

class ConsumerTimeSlotMapping:
    consumer = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(ProvidersTimeSlot, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)