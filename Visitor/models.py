from django.db import models
from django.utils import timezone
from Authenticate.models import Bms_Users

# Create your models here.
class Bms_visiter_details(models.Model):
    user_id=models.ManyToManyField(Bms_Users)
    first_name=models.CharField(max_length=23)
    last_name=models.CharField(max_length=23)
    mobile_no=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=233)
    created_module_date=models.DateTimeField(default=timezone.now)
    updated_module_date=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.first_name
    
    
    class Meta():
        db_table='bms_visiter_details'
        
        
class Bms_visitor_activity(models.Model):
    STATUS=[
        ('Requested','Requested'),
        ('Accepted','Accepted'),
        ('In_progress','In_progress'),
        ('Completed','Completed'),
        ('Cancel','Cancel')
    ]
    user_id=models.ManyToManyField(Bms_visiter_details)
    meeting_person=models.CharField(max_length=23)
    department_name=models.CharField(max_length=23)
    meeting_time=models.TimeField(max_length=32)
    meeting_purpose=models.CharField(max_length=23)
    in_time=models.TimeField()
    out_time=models.TimeField()
    out_remark=models.CharField(max_length=12)
    rfid_id=models.IntegerField()
    status=models.CharField(max_length=23,choices=STATUS)
    access_from_time=models.TimeField()
    access_to_time=models.TimeField()
    access_area=models.TextField()
    locker_id=models.TextField()
    created_module_date=models.DateTimeField(default=timezone.now)
    updated_module_date=models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.meeting_person
    
    class Meta():
        db_table='Bms_visitor_activity'
        
        

    
    
    
