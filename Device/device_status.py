from Device.models import bms_device_information
import json,threading

def getDeviceStatus():
    data = bms_device_information.objects.all()
    d_list = []
    for i in data:
        d = bms_device_information.objects.get(pk=int(i.pk))
        device_info = d.device_informations
        # device_info = json.loads(d.device_informations)
        # print((device_info))
        d_list.append({
            "record_id":d.pk,
            "device_name":d.device_name,
            "device_id": device_info["device_id"] if "device_id" in  device_info else None,
            "channel_id":device_info["channel_id"] if "channel_id" in device_info else None,
            "device_status": device_info["device_status"] if "channel_id" in device_info else None,
        })
    Device_list   = json.dumps(d_list)
    return Device_list
    
