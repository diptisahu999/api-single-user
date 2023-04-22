from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response 
from Authenticate.models import Bms_Roles,Bms_Users,Bms_Users_Details,Bms_Users_register,Bms_Module_master,Bms_Userss
from Authenticate.serializers import BmsUserDetailsSerializer,RoleSerializer,UserSerializer,ModuleSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings



# class LoginView(APIView):
#     def post(self,request,format=None):
#         serializer=BmsUserDetailsSerializer(data=request.data)
#         if serializer.is_valid():
#             user_email=serializer.data.get('user_email')
#             user_password=serializer.data.get('user_password')
#             user=Bms_Users.objects.filter(user_email=user_email,user_password=user_password).first()
#             if user is not None:
#                 userDetails = Bms_Users_Details.objects.all()
#                 tutorials_serializer = UserSerializer(userDetails, many=True)
#                 return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
#             else:
#                 return Response({'error':{'non_field_error':['Email or password is not valid' ]}},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  



def get_tokens_for_user(user):                      # token generated function
    refresh = RefreshToken.for_user(user)

    return {
        # 'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class LoginView(APIView):
    def post(self,request,format=None):
        serializer=BmsUserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            user_email=serializer.data.get('user_email')
            user_password=serializer.data.get('user_password')
            user=Bms_Users.objects.filter(user_email=user_email,user_password=user_password).first()
            # user=authenticate(user_email=user_email,user_password=user_password)
            token=get_tokens_for_user(user)
            subject= 'Account Registation'
            massage=f'Hello Your token is {token}'
            # # send_mail(subject,massage,settings.EMAIL_HOST_USER,self.task_list)
            # send_mail(subject,massage,settings.EMAIL_HOST_USER,['divyeshepandav1999@gmail.com'])
            send_mail(subject,massage,settings.EMAIL_HOST_USER,[user_email])
            
            
            if user is not None:
                userDetails = Bms_Users.objects.all()
                tutorials_serializer = BmsUserDetailsSerializer(userDetails, many=True)
                return Response({"token":token,"data":"true","status_code": "200","message": "Login Successfully", "response":tutorials_serializer.data})
            else:
                return Response({"status_code": "401",'error':{'User not Found':'Email or password is not valid'}},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    
     

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((IsAuthenticated,))
def user_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        bms_users = Bms_Users.objects.all()        
        bms_uses_serializer = BmsUserDetailsSerializer(bms_users, many=True)
        return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":bms_uses_serializer.data})
    
 
    elif request.method == 'POST':
        uses_serializer = BmsUserDetailsSerializer(data=request.data)
        if uses_serializer.is_valid():
            uses_serializer.save()
            # return Response(bms_uses_serializer.data, status=status.HTTP_201_CREATED)
            # return Response({"data":"true","status_code": "200", "message": "User Accounts Create Successfully"})
            return Response({"data":"true","status_code": "200", "message": "User Added Successfully", "response":uses_serializer.data})
         
        return Response(uses_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_Users.objects.all().delete()
        return Response({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
 
 
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def user(request, pk):
    try: 
        bms_users = Bms_Users.objects.get(pk=pk) 
    except Bms_Users.DoesNotExist: 
        return Response({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bms_uses_serializer = BmsUserDetailsSerializer(bms_users) 
        # return Response(bms_uses_serializer.data) 
        return Response({"data":"true","status_code": "200", "message": "User Get Successfully", "response":bms_uses_serializer.data})
        
 
    elif request.method == 'PUT':  
        bms_uses_serializer = BmsUserDetailsSerializer(bms_users, data=request.data) 
        if bms_uses_serializer.is_valid(): 
            bms_uses_serializer.save() 
            # return Response(bms_uses_serializer.data) 
            return Response({"data":"true","status_code": "200", "message": "User Updated Successfully", "response":bms_uses_serializer.data})
            
        return Response(bms_uses_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        Bms_Users.delete() 
        return Response({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def user_list_published(request):
    tutorials = Bms_Users.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = BmsUserDetailsSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data, safe=False)



    
# Role Table Api crud

# def get_tokens_for_user(user):                      # token generated function
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }
   
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((IsAuthenticated,))
def role_list(request):
    # permission_classes=[IsAuthenticated]
    
    if request.method == 'GET':
        bms_role = Bms_Roles.objects.all() 
        bms_role_serializer = RoleSerializer(bms_role, many=True)
        return Response({"data":"true","status_code": "200", "message": "Role lists", "response":bms_role_serializer.data})
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        role_serializer = RoleSerializer(data=request.data)
        if role_serializer.is_valid():
            user=role_serializer.save()
            # token=get_tokens_for_user(user)
            return Response({"data":"true","status_code": "200", "message": "User role created Successfully!!","response":role_serializer.data})
            # return Response({"data":"true","status_code": "200", "message": "User role created Successfully!!",'token':token, "response":tutorial_serializer.data})
        return Response(role_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_Roles.objects.all().delete()
        return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def role_detail(request, pk):
    try: 
        bms_role = Bms_Roles.objects.get(pk=pk)
    except Bms_Roles.DoesNotExist: 
        # return JsonResponse({'message': 'The User Role does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        return Response({'message': 'The User Role does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
 
    if request.method == 'GET': 
        bms_role_serializer = RoleSerializer(bms_role) 
        return Response(bms_role_serializer.data) 
 
    elif request.method == 'PUT': 
        bms_role_serializer = RoleSerializer(bms_role, data=request.data) 
        if bms_role_serializer.is_valid(): 
            bms_role_serializer.save() 
            return Response({"data":"true","status_code": "200", "message": "User Role updated Sucessfuly!!","response":bms_role_serializer.data}) 
        return Response(bms_role_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        bms_role.delete() 
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
        
    
    
# Bms_Users_Details table crud

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((IsAuthenticated,))
def user_details_list(request):
    if request.method == 'GET':
        user_details = Bms_Users_Details.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            user_details = user_details.filter(title__icontains=title)
        
        user_details_serializer = UserSerializer(user_details, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "User Lists", "response":user_details_serializer.data})
 
    elif request.method == 'POST':
        details_serializer = UserSerializer(data=request.data)
        if details_serializer.is_valid():
            details_serializer.save()
            # print(tutorial_serializer.data)
            return Response({"data":"true","status_code": "200", "message": "User Added Sucessfuly!!","response":details_serializer.data}) 
        return Response(details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_Users_Details.objects.all().delete()
        return Response({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def user_detail(request, pk):
    try: 
        user_details = Bms_Users_Details.objects.get(pk=pk) 
    except Bms_Users_Details.DoesNotExist: 
        return Response({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        user_details_serializer = UserSerializer(user_details) 
        return Response(user_details_serializer.data) 
 
    elif request.method == 'PUT': 
        # tutorial_data = JSONParser().parse(request) 
        user_details_serializer = UserSerializer(user_details, data=request.data) 
        if user_details_serializer.is_valid(): 
            user_details_serializer.save() 
            return Response({"data":"true","status_code": "200", "message": "User details updated Sucessfuly!!","response":user_details_serializer.data}) 
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
         
 
    elif request.method == 'DELETE': 
        user_details.delete() 
        return Response({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    



    
# Bms_Module crud



@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((IsAuthenticated,))
def module_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        bms_module = Bms_Module_master.objects.all()        
        bms_module_serializer = ModuleSerializer(bms_module, many=True)
        return Response({"data":"true","status_code": "200", "message": "Module Lists", "response":bms_module_serializer.data})
    
 
    elif request.method == 'POST':
        module_serializer = ModuleSerializer(data=request.data)
        if module_serializer.is_valid():
            module_serializer.save()
            # print(tutorial_serializer.data)
            return Response({"data":"true","status_code": "200", "message": "Module Added Sucessfuly!!","response":module_serializer.data}) 
        return Response(module_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_Module_master.objects.all().delete()
        return Response({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
 
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def module_detail(request, pk):
    try: 
        bms_module = Bms_Module_master.objects.get(pk=pk) 
    except Bms_Module_master.DoesNotExist: 
        return Response({'message': 'The Module does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        module_serializer = ModuleSerializer(bms_module) 
        return Response(module_serializer.data) 
 
    elif request.method == 'PUT': 
        module_serializer = ModuleSerializer(bms_module, data=request.data) 
        if module_serializer.is_valid(): 
            module_serializer.save() 
            return Response({"data":"true","status_code": "200", "message": "Module updated Sucessfuly!!","response":module_serializer.data}) 
        return Response(module_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
         
 
    elif request.method == 'DELETE': 
        bms_module.delete() 
        return Response({'message': 'Module was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
