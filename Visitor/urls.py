from django.urls import path
from .import views


urlpatterns = [
    path('bms_visiter_manage/',views.Bms_Visiter_List),
    path('bms_visiter_manage/<int:pk>',views.Bms_List),
    
    #  path('bms_visiter_manage/',views.List.as_view()),
    #  path('bms_visiter_manage/<int:pk>',views.Lists.as_view()),
     
    
]



