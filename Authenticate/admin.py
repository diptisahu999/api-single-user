from django.contrib import admin
from Authenticate.models import Bms_Module_master,Bms_Roles,Bms_User_Type,Bms_Users,Bms_Users_Details,Bms_Users_register,Bms_Userss
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.


class UserModelAdmin(BaseUserAdmin):
   
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'id','password', 'tc','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credencials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','tc')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name','tc', 'password', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()

@admin.register(Bms_Module_master)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','module_name','module_slug','status','created_module_date','updated_module_date']
    
    
@admin.register(Bms_Roles)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','role_name','created_role_date','updated_role_date']
    
@admin.register(Bms_User_Type)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','created_user_type_date']
    
    
@admin.register(Bms_Users)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','user_email','user_password','status','created_user_date','updated_user_date']
    
    
# @admin.register(Bms_Userss)
# class ModuleAdmin(admin.ModelAdmin):
#     list_display=['id','user_email','user_password','status','created_user_date','updated_user_date']

@admin.register(Bms_Users_Details)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','first_name','phone_no','birthday','address','created_user_details_date','updated_user_details_date']
    
    
# @admin.register(Bms_Users_register)
# class ModuleAdmin(admin.ModelAdmin):
#     list_display=['id','first_name','last_name','phone_no','birthday','address','created_user_details_date','updated_user_details_date']