"""drfsitewc URL Configuration

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
from django.urls import path, include

from wcapi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/themes', ThemesAPIView.as_view()),
    path('api/v1/themes/category', ThemesCategoryAPIView.as_view()),
    path('api/v1/themes/amount', ThemesAmountAPIView.as_view()),
    path('api/v1/add/theme', ThemesThemeAddAPIView.as_view()),
    path('api/v1/delete/theme', ThemesThemeDelAPIView.as_view()),
    path('api/v1/theme/add/widgets', ThemesThemeAddWidgetsAPIView.as_view()),
    path('api/v1/theme/del/widgets', ThemesThemeDelWidgetsAPIView.as_view()),
    path('api/v1/theme/add/icon', ThemesThemeAddIconAPIView.as_view()),
    path('api/v1/theme/del/icon', ThemesThemeDelIconAPIView.as_view()),
    path('api/v1/theme/add/wallpapers', ThemesThemeAddWallpapersAPIView.as_view()),
    path('api/v1/theme/del/wallpapers', ThemesThemeDelWallpapersAPIView.as_view()),
]
