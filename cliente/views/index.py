from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from decouple import config

def index(request):
    return HttpResponse("Documentacion Api RedeDoc")
    
class SaludoView(APIView):
    def get(self, request):
        nombre = config('NOMBRE', default="Sin definir en variable de entorno")
        return Response("Hola mundo " + nombre)    