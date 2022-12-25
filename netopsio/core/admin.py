"""Register core models in admin panel."""

from core.models import RequestLog
from django.contrib import admin


class RequestLogAdmin(admin.ModelAdmin):
    """Request Log Admin Site Fields."""

    list_display = ("ip", "app", "date")


admin.site.register(RequestLog, RequestLogAdmin)
