from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AppleOrder)
admin.site.register(FacebookOrder)
admin.site.register(WalmartOrder)
