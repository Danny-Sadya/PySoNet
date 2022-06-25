from django.contrib import admin
from .models import UserNet


# admin.site.register(UserNet)

@admin.register(UserNet)
class UserNetAdmin(admin.ModelAdmin):
    """UserNet"""
