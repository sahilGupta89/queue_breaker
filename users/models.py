from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=20,null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    location = models.PointField(verbose_name='lat_long',null=True, blank=True,)
    phone = models.TextField(max_length=10,null=False,blank=False)
    birth_date = models.DateField(null=True, blank=True)
    # picture = models.ImageField()
    user_type = models.TextField(max_length=10)
    user_role = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True,null=True)
    deleted = models.BooleanField(default=False)

