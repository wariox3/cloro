from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from pymongo import MongoClient
from decouple import config
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json
import datetime

class EmitirView(APIView):
    def post(self, request):  
        raw = request.data
        documentoMongo = raw
        documentoMongo['fecha'] = datetime.datetime.now(tz=datetime.timezone.utc)
        client = MongoClient(config('DATABASE_MONGO'))
        db = client['cloro']
        collection = db['documento']
        id = collection.insert_one(documentoMongo).inserted_id 
        del documentoMongo["_id"]        
        documentoMongo["id"] = str(id)
        documentoMongo['fecha'] = documentoMongo['fecha'].strftime("%Y-%m-%d %H:%M:%S")              
        with ServiceBusClient.from_connection_string(config('SERVICE_BUS_CONNECTION_STR')) as client:
            with client.get_queue_sender(config('SERVICE_BUS_QUEUE_NAME')) as sender:
                single_message = ServiceBusMessage(json.dumps(documentoMongo))
                sender.send_messages(single_message)
        return Response({"documento:": str(id)}, status=status.HTTP_200_OK)                
