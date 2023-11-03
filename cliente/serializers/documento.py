from cliente.models.documento import Documento, Cuenta, DocumentoClase
from rest_framework import serializers

class DocumentoSerializador(serializers.HyperlinkedModelSerializer):    
    cuenta = serializers.PrimaryKeyRelatedField(queryset=Cuenta.objects.all())
    documento_clase = serializers.PrimaryKeyRelatedField(queryset=DocumentoClase.objects.all())
    class Meta:
        model = Documento
        fields = [
            'prefijo', 
            'numero',
            'fecha',
            'fecha_registro',
            'cuenta',
            'documento_clase'            
        ]  
        
    def validate(self, data):
        cuenta = data.get('cuenta')
        prefijo = data.get('prefijo')
        numero = data.get('numero')
        documento_clase = data.get('documento_clase')

        if Documento.objects.filter(cuenta=cuenta, prefijo=prefijo, numero=numero, documento_clase=documento_clase).exists():
            raise serializers.ValidationError("Ya existe el documento.")

        return data
            
    def to_representation(self, instance):
        return {
            'id': instance.id       
        }        