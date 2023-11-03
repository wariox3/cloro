from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework import status 
from cliente.models.documento import Documento
from cliente.serializers.documento import DocumentoSerializador

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializador   

    def create(self, request):     
        raw = request.data
        documento = raw.get('documento')
        raw['prefijo'] = documento.get('prefijo')
        raw['numero'] = documento.get('numero')
        raw['fecha'] = documento.get('fecha')
        documentoSerializador = DocumentoSerializador(data=raw)
        if documentoSerializador.is_valid():
            documento = documentoSerializador.save()
            return Response("hola", status=status.HTTP_200_OK)    
        return Response(documentoSerializador.errors, status=status.HTTP_400_BAD_REQUEST)