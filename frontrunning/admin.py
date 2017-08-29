from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AppleCustomerOrder)
admin.site.register(AppleFirmOrder)
admin.site.register(FacebookCustomerOrder)
admin.site.register(FacebookFirmOrder)
admin.site.register(WallmartCustomerOrder)
admin.site.register(WalmartFirmOrder)
