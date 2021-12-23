"""Ping App serializers."""

from rest_framework import serializers
from ping.models import PingRequest


class PingRequestSerializer(serializers.ModelSerializer):
    """PingRequest Serializer."""

    class Meta:
        """PingRequest Serializer Meta."""

        model = PingRequest
        fields = ["id", "date", "task_id", "ip", "result", "url"]


class PingSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    """Ping Serializer."""

    task_id = serializers.CharField(max_length=512)
