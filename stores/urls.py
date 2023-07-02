from django.contrib import admin
from django.urls import path, include
from stores.views import StoreView, StoreHoursView, StoreStatusView
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register(r'stores', StoreView)
routers.register(r'storehours', StoreHoursView)
routers.register(r'storestatus', StoreStatusView)

urlpatterns = [
    path('', include(routers.urls)),
]
