from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from stores.models import Store, StoreStatus, StoreHours
from stores.serializers import StoreSerializer, StoreStatusSerializer, StoreHoursSerializer

# Create your views here.

class StoreView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreStatusView(viewsets.ModelViewSet):
    queryset = StoreStatus.objects.all()
    serializer_class = StoreStatusSerializer

class StoreHoursView(viewsets.ModelViewSet):
    queryset = StoreHours.objects.all()
    serializer_class = StoreHoursSerializer