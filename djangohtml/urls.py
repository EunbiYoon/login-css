"""djangohtml URL Configuration

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
from django.urls import path
from appp import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/',admin.site.urls),
    path ('', views.indexView, name="home"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('register/', views.registerView, name="register_url"),
    path('login/',LoginView.as_view(next_page="dashboard"), name="login_url"),
    path('logout/',LogoutView.as_view(next_page="home"), name="logout_url"),
    path('dashboard/bomcomparison',views.bomView, name="dash_bom_url"),
]
