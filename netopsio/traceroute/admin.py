"""Register Ping Models in Admin Pandel."""

from django.contrib import admin
from traceroute.models import TraceRouteRequest


class TraceRouteAdmin(admin.ModelAdmin):
    """TraceRoute Admin Site Fields."""

    list_display = ("ip", "date")


admin.site.register(TraceRouteRequest, TraceRouteAdmin)
