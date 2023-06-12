"""
URL configuration for website_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
#from . import views
from home_page.views import home_view
from login_page.views import login_view
from additional_info.views import additional_info_view
from dashboard.views import dashboard_view
from additional_info.views import delete_user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('login/', login_view, name='login_view'),
    path('addinfo/', additional_info_view, name='additional_info'),
    path('dashboard/', dashboard_view, name="dashboard_view"),
    path('delete/<int:user_id>/', delete_user_view, name='delete_user'),
    
]