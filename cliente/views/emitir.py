from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
import pymongo
import os
from decouple import config
#from cliente.serializer.documento import DocumentoSerializador
#from cliente.models.documento import Documento
#from azure.servicebus import ServiceBusClient, ServiceBusMessage
#from decouple import config
import json

class EmitirView(APIView):
    def post(self, request):  
        client = pymongo.MongoClient(config('DATABASE_MONGO'))
        dbname = client['cloro']
        collection = dbname['documento']
        mascot_1={
            "name": "Sammy",
            "type" : "Shark"
        }
        collection.insert_one(mascot_1)
        return Response('Si señor')
        """raw = request.data
        documento = raw.get('documento')
        documentoSerializador = DocumentoSerializador(data=documento)
        if documentoSerializador.is_valid():
            documentoMongo = documentoSerializador.save()            
            with ServiceBusClient.from_connection_string(config('SERVICE_BUS_CONNECTION_STR')) as client:
                with client.get_queue_sender(config('SERVICE_BUS_QUEUE_NAME')) as sender:
                    single_message = ServiceBusMessage(json.dumps(documento))
                    sender.send_messages(single_message)
            return Response({"documento:": str(documentoMongo.pk)}, status=status.HTTP_200_OK)                
        return Response({'error': documentoSerializador.errors}, status=status.HTTP_400_BAD_REQUEST)"""
