from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app import views


router = DefaultRouter()
router.register('extensions', views.ExtensionViewSet)
router.register('device_model', views.DeviceModelViewSet)
router.register('device_vendor', views.DeviceVendorViewSet)
router.register('dss', views.DSSViewSet)
router.register('device', views.DeviceViewSet)
router.register('customer', views.CustomerViewSet)
# router.register('deviceXML', views.DeviceXML)


app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
    path('deviceXML/', views.DeviceXMLView.as_view())
]
