"""
URL configuration for stock_prediction project
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #BASE API Endpoint
    path('api/v1/', include('api.urls'))
]
