from rest_framework import serializers
from .models import Bms_visiter_details



class Bms_visiter_Serializer(serializers.ModelSerializer): 
    class Meta:
        model = Bms_visiter_details
        fields = "__all__"