"""Register Ping Models in Admin Pandel."""

from django.contrib import admin
from ping.models import PingRequest


class PingAdmin(admin.ModelAdmin):
    """Ping Admin Site Fields."""

    list_display = ("ip", "date")


admin.site.register(PingRequest, PingAdmin)
