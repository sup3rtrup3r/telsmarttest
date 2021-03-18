from rest_framework import viewsets, permissions

from .models import Extension, DeviceModel, DeviceVendor, DSS, Device, Customer

from app.serializers import ExtensionSerializer, DeviceModelSerializer, DeviceVendorSerializer, DSSSerializer, DeviceSerializer, CustomerSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_xml.renderers import XMLRenderer


class ExtensionViewSet(viewsets.ModelViewSet):
    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer
    permissions_classes = [permissions.AllowAny]


class DeviceModelViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer
    permissions_classes = [permissions.AllowAny]


class DeviceVendorViewSet(viewsets.ModelViewSet):
    queryset = DeviceVendor.objects.all()
    serializer_class = DeviceVendorSerializer
    permissions_classes = [permissions.AllowAny]


class DSSViewSet(viewsets.ModelViewSet):
    queryset = DSS.objects.all()
    serializer_class = DSSSerializer
    permissions_classes = [permissions.AllowAny]


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permissions_classes = [permissions.AllowAny]


class MyXMLRenderer(XMLRenderer):
    root_tag_name = 'settings'
    item_tag_name = 'phone-settings'


class DeviceXMLView(APIView):
    renderer_classes = (MyXMLRenderer,)

    def get(self, request):
        device = Device.objects.all()
        device_serializer = DeviceSerializer(device, many=True)
        return Response(device_serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permissions_classes = [permissions.AllowAny]
