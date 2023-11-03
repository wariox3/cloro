from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework import status 
from cliente.models.cuenta import Cuenta
from cliente.serializers.cuenta import CuentaSerializador

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializador    
