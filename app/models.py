from django.db import models
from django.contrib.humanize.templatetags import humanize


class Extension(models.Model):
    name = models.CharField(max_length=64)
    extension = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class DeviceVendor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DeviceModel(models.Model):
    name = models.CharField(max_length=255)
    dss = models.BooleanField()
    """Device model has a vendor"""
    vendor = models.ForeignKey(DeviceVendor, on_delete=models.CASCADE)

    class DeviceFormat(models.TextChoices):
        PDF = "pdf", "PDF"
        HTML = "html", "HTML"
        XML = "xml", "XML"

    device_format = models.CharField("Device format", max_length=255,
                                     choices=DeviceFormat.choices,
                                     default=DeviceFormat.XML)

    def __str__(self):
        return self.name


class DSS(models.Model):
    key = models.IntegerField()
    value = models.CharField(max_length=255)
    label = models.CharField(max_length=255)

    class DssType(models.TextChoices):
        BLF = "blf", "BLF"
        SPD = "spd", "SPD"

    dss_type = models.CharField("Dss type", max_length=45,
                                choices=DssType.choices,
                                default=DssType.SPD)

    def __str__(self):
        return self.label


class Device(models.Model):
    description = models.CharField(max_length=255)
    mac = models.CharField(max_length=255, unique=True)
    cfg_last_update = models.DateTimeField(auto_now_add=True)
    """Device phone has a model"""
    model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    """Device can have multiple DSS's"""
    dss = models.ManyToManyField(DSS)

    def __str__(self):
        return self.description

    def get_cfg_last_update(self):
        return humanize.naturaltime(self.cfg_last_update)


class Customer(models.Model):
    description = models.CharField(max_length=100)
    """Device can be assigned to only one customer"""
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    """Customer can have multiple extensions, but extension can have only one customer"""
    """Extension is unique per customer"""
    extension = models.ForeignKey(Extension,
                                  on_delete=models.CASCADE,
                                  unique=False)

    def __str__(self):
        return self.description
