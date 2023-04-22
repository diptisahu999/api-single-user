from django.contrib import admin
from .models import Bms_visiter_details,Bms_visitor_activity

# Register your models here.

@admin.register(Bms_visiter_details)
class AdminVisiter(admin.ModelAdmin):
    list_display=['id','first_name','last_name']
    
    
@admin.register(Bms_visitor_activity)
class adminVisiter(admin.ModelAdmin):
    list_display=['id','department_name','meeting_purpose']