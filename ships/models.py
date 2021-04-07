from django.core.exceptions import ValidationError
from django.db import models


class Ship(models.Model):
    """Model to represent a ship"""

    name = models.CharField(
        max_length=50,
        verbose_name="Ship name",
    )
    """Ship name"""

    imo = models.IntegerField(
        primary_key=True,
        verbose_name="IMO number",
    )
    """Ship IMO number"""

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if 1000000 <= self.imo <= 9999999:
            return super(Ship, self).save(*args, **kwargs)
        else:
            raise ValidationError("Invalid ship IMO. Needs to be 7 digits")


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    """Primary key"""

    ship_imo = models.ForeignKey(
        Ship,
        related_name="positions",
        on_delete=models.CASCADE,
        verbose_name="Ship IMO",
    )
    """Ship IMO FK"""

    timestamp = models.DateTimeField(verbose_name="Position timestamp")
    """Position timestamp"""

    latitude = models.FloatField()
    """Position latitude"""

    longitude = models.FloatField()
    """Position longitude"""

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.latitude < -90 or self.latitude > 90:
            raise ValidationError("Invalid latitude")
        elif self.longitude < -180 or self.longitude > 180:
            raise ValidationError("Invalid longitude")
        else:
            return super(Position, self).save(*args, **kwargs)
