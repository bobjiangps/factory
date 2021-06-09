"""factory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from factory.settings import registered
from rest_framework import routers
from users import views_auth_token as uat_views


router = routers.DefaultRouter()


role_url = {
    "office": path('factory/api/office/', include('office.urls')),
    "worker": path('factory/api/worker/', include('worker.urls'))
}

urlpatterns = [
    path('factory/api/', include(router.urls)),
    role_url[registered["role"]],
    path('admin/', admin.site.urls),
    path('factory/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('factory/api/login/', uat_views.ObtainExpiringAuthToken.as_view(), name='login'),
    path('factory/api/logout/', uat_views.RevokeAuthToken.as_view(), name='logout'),
]
