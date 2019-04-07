"""django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from main.views import index,week1,list_add,list_finsh,del_completed
from rest_framework import routers
from week2.views import MessagesViewSet
from week3.views import SpiderViewSet
from week4.views import FaceViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessagesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('week1/', week1,name='week1'),
    path('list_add/', list_add, name='list_add'),
    path('list_finsh/<list_id>/', list_finsh, name='list_finsh'),
    path('del_completed/', del_completed, name='del_completed'),
    path('week2/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('week3/', SpiderViewSet, name='week3'),
    path('week4/', FaceViewSet, name='week4'),
    # path('week4/', FaceViewSet, name='week4'),
]
