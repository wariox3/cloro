from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

def index(request):
    return HttpResponse("Documentacion Api RedeDoc")
    
class SaludoView(APIView):
    def get(self, request):
        return Response("Hola mundo")    