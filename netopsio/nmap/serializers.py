"""Nmap App serializers."""

from rest_framework import serializers
from nmap.models import NmapRequest


class NmapRequestSerializer(serializers.ModelSerializer):
    """NmapRequest Serializer."""

    class Meta:
        """NmapRequest Serializer Meta."""

        model = NmapRequest
        fields = ["id", "date", "task_id", "ip", "result", "url"]


class NmapSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    """Nmap Serializer."""

    task_id = serializers.CharField(max_length=512)
