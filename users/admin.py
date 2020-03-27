from django.contrib import admin
from .models import User,Location,PhoneTokens,AccessTokens

admin.site.register(User)
admin.site.register(Location)
# admin.site.register(Role)
admin.site.register(PhoneTokens)
admin.site.register(AccessTokens)