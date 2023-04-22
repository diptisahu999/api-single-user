from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bms_visiter_details
from .serializers import Bms_visiter_Serializer
from django.http.response import JsonResponse
from rest_framework.views import APIView



# Create your views here.

@api_view(['GET',"POST",'DELETE'])
def Bms_Visiter_List(request):
    if request.method=="GET":
        visitor=Bms_visiter_details.objects.all()
        visitor_serializer=Bms_visiter_Serializer(visitor,many=True)
        return Response({'status':'true','responce':visitor_serializer.data})
    
    
    elif request.method=="POST":
        Visitor_Serializer=Bms_visiter_Serializer(data=request.data)
        if Visitor_Serializer.is_valid():
            Visitor_Serializer.save()
            return Response(Visitor_Serializer.data)
        
        
    if request.method=="DELETE":
        Bms_visiter_details.objects.all().delete()
        return Response({'msg':"delete Visiter Succesfully!!"})
    
    
@api_view(["GET",'PUT',"DELETE"])
def Bms_List(request,pk):
    
    try: 
        visitor = Bms_visiter_details.objects.get(pk=pk) 
    except Bms_visiter_details.DoesNotExist: 
        return Response({'message': 'The Visitor does not exist'}) 
    
    
    if request.method=='GET':
        # visitor=Bms_visiter_details.objects.get(pk=pk)
        visitor_serial=Bms_visiter_Serializer(visitor)
        return Response(visitor_serial.data)
    
    
    elif request.method=="PUT":
        # visitors=Bms_visiter_details.objects.get(pk=pk)
        visitor_Serializer=Bms_visiter_Serializer(visitor,data=request.data)
        if visitor_Serializer.is_valid():
            visitor_Serializer.save()
            return Response(visitor_Serializer.data)
        
        
    elif request.method=='DELETE':
        visitor.delete()
        return Response({'msg':"delete Visiter Succesfully!!"})
    
    
# class List(APIView):
#     def get(self,request):
#         visitor=Bms_visiter_details.objects.all()
#         Visiter_Serializer=Bms_visiter_Serializer(visitor,many=True)
#         return Response(Visiter_Serializer.data)
    
    
#     def post(self,request):
#         Visitor_Serializer=Bms_visiter_Serializer(data=request.data)
#         if Visitor_Serializer.is_valid():
#             Visitor_Serializer.save()
#             return Response(Visitor_Serializer.data)
        
        
#     def delete(self,request):
#         Bms_visiter_details.objects.all().delete()
#         return Response({'msg':'delete data succesfully!!!'})
    
    
# class Lists(APIView):
#     def get(self,request,pk):
#         visitor=Bms_visiter_details.objects.get(pk=pk)
#         visitor_serializer=Bms_visiter_Serializer(visitor)
#         return Response(visitor_serializer.data)
    
    
#     def put(self,request,pk):
#         visitor=Bms_visiter_details.objects.get(pk=pk)
#         visitor_Serializer=Bms_visiter_Serializer(visitor,data=request.data)
#         if visitor_Serializer.is_valid():
#             visitor_Serializer.save()
#             return Response(visitor_Serializer.data)
        
#     def delete(self,request,pk):
#         visitor=Bms_visiter_details.objects.get(pk=pk)
#         visitor.delete()
#         return Response({'msg':'delete Succesfully!!!'})
        
        
    
        
        
    
    

            
        
