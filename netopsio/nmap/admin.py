"""Register Nmap Models in Admin Pandel."""

from django.contrib import admin
from nmap.models import NmapRequest


class NmapAdmin(admin.ModelAdmin):
    """Nmap Admin Site Fields."""

    list_display = ("ip", "date")


admin.site.register(NmapRequest, NmapAdmin)
