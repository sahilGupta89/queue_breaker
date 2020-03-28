# from django.contrib.gis.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


# class Role(models.Model):
#     '''
#   The Role entries are managed by the system,
#   automatically created via a Django data migration.
#   '''
#     CONSUMER = 1
#     PROVIDER = 2
#     ADMIN = 5
#
#     ROLE_CHOICES = (
#         (CONSUMER, 'consumer'),
#         (PROVIDER, 'provider'),
#         (ADMIN, 'admin'),
#     )
#
#     id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
#
#     def __int__(self):
#         return self.get_id_display()


class User(AbstractBaseUser):
    CONSUMER = 1
    PROVIDER = 2
    ADMIN = 5

    ROLE_CHOICES = (
        (CONSUMER, 'consumer'),
        (PROVIDER, 'provider'),
        (ADMIN, 'admin'),
    )

    phone = models.TextField(max_length=10, unique=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/profile/', null=True, blank=True)
    roles = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=CONSUMER)
    # roles = models.ManyToManyField(Role)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['phone']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.phone

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", null=True)
    # phone = models.TextField(max_length=12,blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    street = models.TextField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True),
    lat = models.DecimalField(verbose_name='lattitude', max_digits=8, decimal_places=5, default=00.00000)
    lng = models.DecimalField(verbose_name='longitude', max_digits=8, decimal_places=5, default=00.00000)

    def __str__(self):
        return self.user.phone


class PhoneTokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # phone = models.TextField(max_length=12, null=False, blank=True)
    otp_sent = models.BooleanField(default=False)
    otp = models.BigIntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone


class AccessTokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.TextField(null=True)
    refresh_token = models.TextField(null=True)

    def __str__(self):
        return self.user
