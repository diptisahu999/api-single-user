from rest_framework import serializers 
from Authenticate.models import Bms_Module_master,Bms_Roles,Bms_User_Type,Bms_Users,Bms_Users_Details,Bms_Users_register,Bms_Userss
from Device.models import bms_department_master,bms_locker
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from Authenticate.utils import Util
from xml.dom import ValidationErr





class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_Module_master
        fields='__all__'
 
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_Roles
        fields=['id','role_name','permissions_id']
        
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_User_Type
        fields=['id','user_type_name']        
        
        
class DepertmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=bms_department_master
        fields=['department_name'] 
        
class lockerSerializer(serializers.ModelSerializer):
    class Meta:
        model=bms_locker
        fields=['locker_name']
         
class BmsUserSerializer(serializers.ModelSerializer):
    # user_type_id=UserTypeSerializer(many=True,read_only=True)
    role_id=RoleSerializer(many=True,read_only=True)
    department_id=DepertmentSerializer(many=True,read_only=True)
    locker_id=lockerSerializer(many=True,read_only=True)
    class Meta:
        model = Bms_Users_Details
        fields = '__all__'
        
class BmsUserDetailsSerializer(serializers.ModelSerializer):
    # user_type=UserTypeSerializer(many=True,read_only=True)
    role_id=RoleSerializer(many=True,read_only=True)
    user_details=BmsUserSerializer(many=True,read_only=True)
    # user_email=serializers.EmailField(blank=True, null=True)
    # user_password=serializers.CharField(max_length=23)
        
    
    class Meta:
        model = Bms_Userss
        fields = '__all__'
        
    # def validate(self,attrs):
    #     email=attrs.get('user_email')
    #     if Bms_Users.objects.filter(email=email).exists():
    #         user=Bms_Users.objects.get(email=email)
    #         udi=urlsafe_base64_encode(force_bytes(user.id))
    #         print('encode UID',udi)
    #         token=PasswordResetTokenGenerator().make_token(user)
    #         print('password resend token',token)
    #         link='http://localhost:3000/'+ udi + '/' + token
    #         print('password resend token',link)
    #         #send email
    #         body='Click following Link To Resert Your Password:'  +link
    #         data={
    #             'subject':'Reset your password',
    #             'body':body,
    #             'to':user.email
                    
    #         }
    #         Util.send_mail(data)
    #         return attrs
    #     else:
    #         raise ValidationErr('You are not a registation uesr')    
        

# user registation        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bms_Users_Details
        fields = '__all__'
        
        
        
#user Views
class Manage_user_view(serializers.ModelSerializer):
    class Meta:
        model = '__all__'
        
        
# class SendPasswordToEmail(serializers.ModelSerializer):
#     email=serializers.EmailField(max_length=223)
#     class Meta:
#         model=Bms_Users
#         fields=['email']
        
#     def validate(self,attrs):
#         email=attrs.get('email')
#         if Bms_Users.objects.filter(email=email).exists():
#             user=Bms_Users.objects.get(email=email)
#             udi=urlsafe_base64_encode(force_bytes(user.id))
#             print('encode UID',udi)
#             token=PasswordResetTokenGenerator().make_token(user)
#             print('password resend token',token)
#             link='http://localhost:3000/'+ udi + '/' + token
#             print('password resend token',link)
#             #send email
#             body='Click following Link To Resert Your Password:'  +link
#             data={
#                 'subject':'Reset your password',
#                 'body':body,
#                 'to':user.email
                    
#             }
#             Util.send_mail(data)
#             return attrs
#         else:
#             raise ValidationErr('You are not a registation uesr')