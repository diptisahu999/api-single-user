"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import threading
from BMS import device_control
from Device import device_status
from Device import device_control



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Authenticate.urls')),
    path('',include('Device.urls')),
    # path('',include('Inventory.urls')),
    path('',include('Visitor.urls')),
]
# device_control.main_config()
# jsonUpdator = threading.Thread(target=device_control.client_main_config())
# jsonUpdator.start()
# device_control.client_main_config()
# threading.Thread(target=device_status.getDeviceStatus())

# device_status.getDeviceStatus()


# back to the server for every subsequent request, 
# so the server knows the request comes from a particular identity.