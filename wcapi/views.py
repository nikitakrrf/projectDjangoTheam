from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

#from .models import Wcapi
from .serializers import WcapiSerializer

#class WcapiAPIView(APIView):
#    def get(self,request):
#        lst = Wcapi.objects.all().values()
#        return Response({'users': list(lst)})
