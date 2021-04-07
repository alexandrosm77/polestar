from rest_framework import serializers

from .models import Position, Ship


class ShipSerializer(serializers.ModelSerializer):
    """Ship model serializer"""

    class Meta:

        model = Ship
        fields = ("name", "imo")


class PositionSerializer(serializers.ModelSerializer):
    """Position model serializer"""

    class Meta:

        model = Position
        fields = ("ship_imo", "timestamp", "latitude", "longitude")
        lookup_field = "ship_imo"
