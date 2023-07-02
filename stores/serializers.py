from rest_framework import serializers
from stores.models import Store, StoreStatus, StoreHours

# create serializer here

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="stores:store-detail")
    class Meta:
        model = Store
        fields = "__all__"

class StoreStatusSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="stores:storestatus-detail")
    class Meta:
        model = StoreStatus
        fields = "__all__"

class StoreHoursSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="stores:storehours-detail")
    class Meta:
        model = StoreHours
        fields = "__all__"