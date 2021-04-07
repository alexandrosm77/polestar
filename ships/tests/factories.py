import factory
from django.utils import timezone
from faker import Faker

from ..models import Position, Ship

FAKER = Faker()


class ShipFactory(factory.django.DjangoModelFactory):
    """Factory for the Ship model"""

    class Meta:
        model = Ship

    name = factory.lazy_attribute(lambda _: FAKER.name())
    imo = factory.lazy_attribute(
        lambda _: FAKER.pyint(min_value=1000000, max_value=9999999)
    )


class PositionFactory(factory.django.DjangoModelFactory):
    """Factory for the Position model"""

    class Meta:
        model = Position

    ship_imo = factory.SubFactory(ShipFactory)
    timestamp = factory.LazyAttribute(
        lambda _: FAKER.date_time_between(
            start_date="-20d", tzinfo=timezone.utc
        )
    )
    latitude = factory.LazyAttribute(
        lambda _: FAKER.pyfloat(min_value=-90, max_value=90)
    )
    longitude = factory.LazyAttribute(
        lambda _: FAKER.pyfloat(min_value=-180, max_value=180)
    )
