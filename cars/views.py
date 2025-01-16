from rest_framework import viewsets, permissions
from cars.models import Brand, Car
from cars.serializers import BrandModelSerializer, CarModelSerializer
from dj_rql.drf import RQLFilterBackend
from cars.filters import BrandFilterClass, CarFilterClass
from cars.permissions import CarOwnerPermission

# Create your views here.


class BrandModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar marcas (Brand).
    """
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = BrandFilterClass


class CarModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar carros (Car).
    """
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CarFilterClass
    permission_classes = [CarOwnerPermission]  # Apenas CarOwnerPermission será aplicada
