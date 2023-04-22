from rest_framework import serializers 

from Device.models import *

class Bms_Bulding_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=bms_building_master
        fields=['id','tower_name']
        
        
class Bms_floor_master_Serializer(serializers.ModelSerializer):
    tower_id=Bms_Bulding_master_Serializer(many=True,read_only=True)   
    class Meta:
        model=bms_floor_master
        fields='__all__'
        
class Bms_floor_master_Serializers(serializers.ModelSerializer):
    class Meta:
        model=bms_floor_master
        fields='__all__'
        
        
class Bms_department_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=bms_department_master
        fields='__all__'
        
        
class Bms_sub_area_master_Serializer(serializers.ModelSerializer):
    # tower_id=Bms_Bulding_master_Serializer(many=True,read_only=True)
    class Meta:
        model=bms_sub_area_master
        fields='__all__'
        
        
class Bms_locker_Serializer(serializers.ModelSerializer):
    class Meta:
        model=bms_locker
        fields=['id','locker_name','category','status']



class Bms_Devices_Serializer(serializers.ModelSerializer):
    class Meta:
        model= bms_device_information

        fields='__all__'



class Bms_hardware_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model= bms_hardware_type_master

        fields='__all__'



class Bms_device_status_history_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Bms_device_status_history

        fields='__all__'

    
class Bms_device_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model= bms_device_type_master

        fields='__all__'
        

class Bms_user_area_cards_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model= bms_user_area_cards_List

        fields='__all__'


class bms_building_floor_area_subarea_device_Serializer(serializers.ModelSerializer):
    class Meta:
        floor=Bms_floor_master_Serializer(many=True,read_only=True)
        area=Bms_sub_area_master_Serializer(many=True,read_only=True)
        subarea =Bms_sub_area_master_Serializer(many=True,read_only=True)                                                                                                       
        building =Bms_Bulding_master_Serializer(many=True,read_only=True)
        device =Bms_Devices_Serializer(many=True,read_only=True)
        



    class Meta:
        model = bms_sub_area_master
        fields = '__all__'


class bms_area_Serializer(serializers.ModelSerializer):
    # floor_id=Bms_floor_master_Serializer(many=True,read_only=True)
    class Meta:
        model= bms_area_master
        fields='__all__'
        
        
class bms_area_Serializers(serializers.ModelSerializer):
    # floor_id=Bms_floor_master_Serializer(many=True,read_only=True)
    tower_id=Bms_Bulding_master_Serializer(many=True,read_only=True)
    class Meta:
        model= bms_area_master
        fields='__all__'