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
    home_delivery = models.BooleanField(default=False)
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
    PENDING = 1
    FAILED = 2
    COMPLETED = 3
    CANCELED = 4
    booking_status = (
        (PENDING, 'Pending'),
        (FAILED, 'Failed'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    )

    consumer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False,related_name='consumertimeslots')
    time_slot = models.ForeignKey(ProvidersTimeSlot, on_delete=models.CASCADE),
    booking_status = models.PositiveSmallIntegerField(choices=booking_status, blank=True, null=True, default=PENDING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.consumer.phone


class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.TextField(blank=True,null=True)
    color = models.CharField(max_length=32,null=True,blank=True)
    is_sent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.msg


class AppVersion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    version = models.DecimalField(max_digits=12, decimal_places=5, default=00.00000)
    last_updated = models.DateTimeField(blank=True, null=True)
    force_update = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.version)