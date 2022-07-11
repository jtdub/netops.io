"""TraceRoute App serializers."""

from rest_framework import serializers
from traceroute.models import TraceRouteRequest


class TraceRouteRequestSerializer(serializers.ModelSerializer):
    """TraceRouteRequest Serializer."""

    class Meta:
        """TraceRouteRequest Serializer Meta."""

        model = TraceRouteRequest
        fields = ["id", "date", "task_id", "ip", "result", "url"]


class TraceRouteSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    """TraceRoute Serializer."""

    task_id = serializers.CharField(max_length=512)
