from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from ..models import Position, Ship
from ..serializers import PositionSerializer, ShipSerializer
from .factories import PositionFactory, ShipFactory

client = Client()


class GetAllShipsTest(TestCase):
    """ Test module for GET all ships API """

    def setUp(self):
        self.ships = ShipFactory.create_batch(size=10)
        self.url = reverse("ships-list")

    def test_get_all_ships(self):
        """Test get all ships endpoint"""
        response = client.get(self.url)
        ships = Ship.objects.all()
        serializer = ShipSerializer(ships, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_no_ships_exist(self):
        """Test get all ships endpoint when no ships exist"""
        Ship.objects.all().delete()
        response = client.get(self.url)
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetShipPositionsTestCase(TestCase):
    """Testcase for GET positions endpoint"""

    def setUp(self) -> None:
        self.ship = ShipFactory.create()
        self.positions = PositionFactory.create_batch(
            size=10, ship_imo=self.ship
        )
        self.url = reverse(
            "positions-list",
            kwargs={"ship_imo": self.ship.imo}
        )

    def test_get_positions(self):
        """Test getting all positions for a ship in the required order"""
        response = client.get(self.url)
        positions = Position.objects.all().order_by("-timestamp")
        serializer = PositionSerializer(positions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_positions_not_existing(self):
        """Test getting all positions for a ship when they dont exist"""
        Position.objects.all().delete()
        response = client.get(self.url)
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
