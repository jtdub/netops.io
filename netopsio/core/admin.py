"""Register core models in admin panel."""

from django.contrib import admin
from core.models import RequestLog


class RequestLogAdmin(admin.ModelAdmin):
    """Request Log Admin Site Fields."""

    list_display = ("ip", "app", "date")


admin.site.register(RequestLog, RequestLogAdmin)
