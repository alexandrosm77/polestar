from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from ships.models import Position, Ship


class ShipTest(TestCase):
    """Test the Ship model"""

    def setUp(self) -> None:
        self.ship = Ship.objects.create(name="Test ship", imo=1234567)

    def test_ship_string(self):
        """Test the ship string"""
        self.assertEqual(str(self.ship), self.ship.name)

    def test_ship_imo_length(self):
        """Test for invalid IMO length"""
        with self.assertRaises(ValidationError) as ctx:
            Ship.objects.create(name="A test ship", imo=123)
        self.assertEqual(
            str(ctx.exception), "['Invalid ship IMO. Needs to be 7 digits']"
        )


class PositionTestCase(TestCase):
    """Test the Position model"""

    def setUp(self) -> None:
        self.ship = Ship.objects.create(name="Test Ship", imo=1234567)
        self.position = Position.objects.create(
            ship_imo=self.ship,
            timestamp=timezone.now(),
            latitude=51.8,
            longitude=2.68
        )

    def test_position_string(self):
        """Test the position string"""
        self.assertEqual(str(self.position), str(self.position.id))

    def test_invalid_latitude(self):
        """Test invalid Position latitude"""
        for latitude in [-100, 100]:
            with self.assertRaises(ValidationError) as ctx:
                Position.objects.create(
                    ship_imo=self.ship,
                    timestamp=timezone.now(),
                    latitude=latitude,
                    longitude=0,
                )
            self.assertEqual(str(ctx.exception), "['Invalid latitude']")

    def test_invalid_longitude(self):
        """Test invalid Position longitude"""
        for longitude in [-190, 190]:
            with self.assertRaises(ValidationError) as ctx:
                Position.objects.create(
                    ship_imo=self.ship,
                    timestamp=timezone.now(),
                    latitude=0,
                    longitude=longitude,
                )
            self.assertEqual(str(ctx.exception), "['Invalid longitude']")
