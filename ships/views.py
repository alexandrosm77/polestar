from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Position, Ship
from .serializers import PositionSerializer, ShipSerializer


class ShipViewSet(mixins.ListModelMixin, GenericViewSet):
    """GET ships viewset"""

    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class PositionViewSet(mixins.ListModelMixin, GenericViewSet):
    """GET positions for a ship viewset"""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    lookup_field = "ship_imo"

    def get_queryset(self):
        """
        This view should return a list of all the positions
        for a given ship
        """
        return Position.objects.filter(
            ship_imo=self.kwargs.get("ship_imo")
        ).order_by("-timestamp")
