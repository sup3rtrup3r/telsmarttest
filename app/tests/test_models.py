from django.test import TestCase

from .factories import ExtensionFactory, DeviceVendorFactory, DeviceModelFactory, DSSFactory, DeviceFactory, CustomerFactory


class ModelTests(TestCase):

    def test_str_extension(self):
        extension = ExtensionFactory(name="extension")
        self.assertEqual(str(extension), extension.name)

    def test_str_devicevendor(self):
        devicevendor = DeviceVendorFactory(name="devicevendor")
        self.assertEqual(str(devicevendor), devicevendor.name)

    def test_str_devicemodel(self):
        devicemodel = DeviceModelFactory(name="devicemodel")
        self.assertEqual(str(devicemodel), devicemodel.name)

    def test_str_dss(self):
        dss = DSSFactory(label="dss")
        self.assertEqual(str(dss), dss.label)

    def test_str_device(self):
        device = DeviceFactory(description="device majami vice")
        self.assertEqual(str(device), device.description)

    def test_str_customer(self):
        customer = CustomerFactory(description="customer")
        self.assertEqual(str(customer), customer.description)
