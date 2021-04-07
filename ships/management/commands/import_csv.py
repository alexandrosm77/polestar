import csv

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.dateparse import parse_datetime

from ships.models import Position, Ship


class Command(BaseCommand):
    help = "Import positions csv"

    def add_arguments(self, parser):
        parser.add_argument("filename", type=str)

    def handle(self, *args, **options):
        ships = [
            {9632179: "Mathilde Maersk"},
            {9247455: "Australian Spirit"},
            {9595321: "MSC Preziosa"},
        ]

        for ship in ships:
            for imo, name in ship.items():
                Ship.objects.get_or_create(name=name, imo=imo)

        try:
            with transaction.atomic():
                with open("positions.csv") as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        Position.objects.get_or_create(
                            ship_imo=Ship.objects.get(imo=int(row[0])),
                            timestamp=parse_datetime(row[1]),
                            latitude=float(row[2]),
                            longitude=float(row[3]),
                        )
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully imported {options["filename"]}'
                )
            )
        except Exception as e:
            self.stderr.write(
                f'Error importing {options["filename"]}. Exception {str(e)}'
            )
