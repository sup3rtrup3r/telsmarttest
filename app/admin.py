from django.contrib import admin
from django.db.models import Count

from app import models


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(DeviceAdmin, self).get_queryset(request)
        return qs.annotate(dss_count=Count('dss'))

    def dss_count(self, inst):
        return inst.dss_count

    actions = ["download_device_config"]

    def download_device_config(self, request, queryset):
        pass

    download_device_config.short_description = "DDC"

    search_fields = ('description', 'mac', 'model__name', 'customer__description')
    list_filter = ('customer', 'model',)
    list_display = ('description', 'get_cfg_last_update', 'dss_count', )
    list_per_page = 10


admin.site.register(models.Extension)
admin.site.register(models.DeviceVendor)
admin.site.register(models.DeviceModel)
admin.site.register(models.DSS)
admin.site.register(models.Customer)
