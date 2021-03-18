from django.db import transaction
from django.core.management.base import BaseCommand

from app.models import Extension, DeviceVendor, DeviceModel, DSS, Device, Customer
from app.tests.factories import CustomerFactory, DSSFactory

NUM_CUSTOMERS = 50


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Extension, DeviceVendor, DeviceModel, DSS, Device, Customer]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        for _ in range(NUM_CUSTOMERS):
            DSSFactory()
            CustomerFactory()
