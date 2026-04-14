"""
URL configuration for Banking_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.account_list, name='account_list'),
    path('add/', views.add_account, name='add_account'),
    path('update/<int:id>/', views.update_account, name='update_account'),
    path('delete/<int:id>/', views.delete_account, name='delete_account'),
    path('deposit/<int:id>/', views.deposit, name='deposit'),
    path('withdraw/<int:id>/', views.withdraw, name='withdraw'),
]
