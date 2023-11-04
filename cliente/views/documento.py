from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import action
from cliente.models.documento import Documento
from cliente.serializers.documento import DocumentoSerializador
from pymongo import MongoClient
from decouple import config
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from django.http import HttpResponse
import json
from utilidades.xml import Xml

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
            documentoMongo = raw
            client = MongoClient(config('DATABASE_MONGO'))
            db = client['cloro']
            collection = db['documento']            
            id = collection.insert_one(documentoMongo).inserted_id     
            #xml = Xml()
            #prueba = xml.generar()       
            #del documentoMongo["_id"]        
            #documentoMongo["id"] = str(id)
            #documentoMongo['fecha'] = documentoMongo['fecha'].strftime("%Y-%m-%d %H:%M:%S")              
            #with ServiceBusClient.from_connection_string(config('SERVICE_BUS_CONNECTION_STR')) as client:
            #    with client.get_queue_sender(config('SERVICE_BUS_QUEUE_NAME')) as sender:
            #        single_message = ServiceBusMessage(json.dumps(documentoMongo))
            #        sender.send_messages(single_message)
            documento = documentoSerializador.save()            
            return Response("Documento creado", status=status.HTTP_200_OK)    
        return Response(documentoSerializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=["post"], url_path=r'xml',)
    def lista(self, request):
        raw = request.data
        cuenta = raw.get('cuenta')
        documento_clase = raw.get('documento_clase')
        prefijo = raw.get('prefijo')
        numero = raw.get('numero')
        if cuenta and documento_clase and prefijo and numero:
            try:
                documento = Documento.objects.get(cuenta=cuenta, documento_clase=documento_clase, prefijo=prefijo, numero=numero)
                xml = Xml()
                documentoXml = xml.generar()                  
                return HttpResponse(documentoXml, content_type='application/xml')
            except Documento.DoesNotExist:                                            
                return Response('El documento no existe', status=status.HTTP_400_BAD_REQUEST)        
        return Response('Faltan parametros', status=status.HTTP_400_BAD_REQUEST)