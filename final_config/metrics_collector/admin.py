from django.contrib import admin
from .models import Client, Metrics


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'name', 'description')

