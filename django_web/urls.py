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
from main import views
from rest_framework import routers
from week2.views import MessagesViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessagesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('week1/', views.week1,name='week1'),
    path('list_add/', views.list_add, name='list_add'),
    path('list_finsh/<list_id>/', views.list_finsh, name='list_finsh'),
    path('del_completed/', views.del_completed, name='del_completed'),
    path('week2/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
