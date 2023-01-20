from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WcapiSerializer

class ThemesAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})


class ThemesCategoryAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})


class ThemesAmountAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})


class ThemesThemeAddAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})


class ThemesThemeDelAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})

class ThemesThemeAddWidgetsAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})

class ThemesThemeDelWidgetsAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})


class ThemesThemeAddIconAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})


class ThemesThemeDelIconAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})


class ThemesThemeAddWallpapersAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})

class ThemesThemeDelWallpapersAPIView(APIView):
    def get(self,request):
        return Response({'test': 'test'})

    def post(self,request):
        return Response({'test': 'test'})