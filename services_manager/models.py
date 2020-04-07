# from django.contrib.gis.db import models
from django.db import models
from users.models import User


class Categories(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='catagories/', null=True, blank=True)
    subcategories = models.ManyToManyField('self', symmetrical=False,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProvidersTimeSlot(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False,related_name='providertimeslots')
    start_time = models.DateTimeField(verbose_name='service start time')
    end_time = models.DateTimeField(verbose_name='service end time')
    day = models.CharField(verbose_name='days of week',max_length=10, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.provider.phone


class ProviderCategoryMapping(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False,related_name='providercategorymappings')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.provider.phone


class ConsumerTimeSlotMapping(models.Model):
    consumer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False,related_name='consumertimeslots')
    time_slot = models.ForeignKey(ProvidersTimeSlot, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.consumer.phone