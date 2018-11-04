"""unicrud URL Configuration

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
from django.urls import path
from catalog.views import *

urlpatterns = [
    path('insert/', insert_view, name='insert_view'),
    path('list/', list_view, name='list_view'),
    path('import/', import_view, name='import_view'),
    path('report/', report_view, name='report_view'),
    path('delete/', delete_view, name='delete_view'),
    path('update/', update_view, name='update_view'),
]
