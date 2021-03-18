import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from django.utils import timezone

from app.models import Extension, DeviceVendor, DeviceModel, DSS, Device, Customer


class ExtensionFactory(DjangoModelFactory):
    class Meta:
        model = Extension
        django_get_or_create = ('name',)

    name = factory.Faker("first_name")
    extension = factory.fuzzy.FuzzyInteger(1000000)


class DeviceVendorFactory(DjangoModelFactory):
    class Meta:
        model = DeviceVendor
        django_get_or_create = ('name',)

    name = factory.Faker("first_name")


class DeviceModelFactory(DjangoModelFactory):
    class Meta:
        model = DeviceModel

    name = factory.Faker("first_name")
    dss = 'True'
    vendor = factory.SubFactory(DeviceVendorFactory)
    device_format = factory.fuzzy.FuzzyChoice(
        [x[0] for x in DeviceModel.DeviceFormat.choices]
    )


class DSSFactory(DjangoModelFactory):
    class Meta:
        model = DSS

    key = factory.fuzzy.FuzzyInteger(1000000)
    value = factory.fuzzy.FuzzyText(length=8)
    label = factory.fuzzy.FuzzyText(length=12)
    dss_type = factory.fuzzy.FuzzyChoice(
        [x[0] for x in DSS.DssType.choices]
    )


class DeviceFactory(DjangoModelFactory):
    class Meta:
        model = Device
    description = factory.Faker("sentence", nb_words=11, variable_nb_words=True)
    mac = factory.fuzzy.FuzzyText()
    cfg_last_update = factory.LazyFunction(timezone.now)
    model = factory.SubFactory(DeviceModelFactory)
    @factory.post_generation
    def dsss(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for dss in extracted:
                self.dsss.add(dss)


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    description = factory.Faker("sentence", nb_words=7, variable_nb_words=True)
    device = factory.SubFactory(DeviceFactory)
    extension = factory.SubFactory(ExtensionFactory)
