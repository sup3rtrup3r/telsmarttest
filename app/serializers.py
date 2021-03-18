from rest_framework import serializers

from .models import Extension, DeviceModel, DeviceVendor, DSS, Device, Customer


class ExtensionSerializer(serializers.ModelSerializer):
    """Serializer for extension objects"""

    class Meta:
        model = Extension
        fields = ('pk', 'name', 'extension')
        # read_only_fields = ('name',)


class DeviceVendorSerializer(serializers.ModelSerializer):
    """Serializer for device vendor objects"""

    class Meta:
        model = DeviceVendor
        fields = ('id', 'name')
        # read_only_fields = ('name',)


class DeviceModelSerializer(serializers.ModelSerializer):
    """Serializer a device model objects"""

    class Meta:
        model = DeviceModel
        fields = ('pk', 'name', 'dss', 'vendor', 'device_format')
        # read_only_fields = ('id',)


class DSSSerializer(serializers.ModelSerializer):
    """Serializer for DSS model objects"""

    class Meta:
        model = DSS
        fields = ('pk', 'key', 'value', 'label')
        # read_only_fields = ('label',)


class DeviceSerializer(serializers.ModelSerializer):
    """Serializer for device model objects"""

    class Meta:
        model = Device
        fields = ('pk', 'description', 'mac', 'cfg_last_update', 'model', 'dss')


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for customer model objects"""

    class Meta:
        model = Customer
        fields = ('pk', 'description', 'device', 'extension')
