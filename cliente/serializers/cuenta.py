from cliente.models.cuenta import Cuenta, Ciudad, Identificacion
from rest_framework import serializers

class CuentaSerializador(serializers.HyperlinkedModelSerializer):
    identificacion = serializers.PrimaryKeyRelatedField(queryset=Identificacion.objects.all())
    ciudad = serializers.PrimaryKeyRelatedField(queryset=Ciudad.objects.all())    
    class Meta:
        model = Cuenta
        fields = [
            'identificacion', 
            'numero_identificacion',
            'nombre',
            'ciudad',
            'celular',
            'correo',
        ]  
        
    def validate(self, data):
        numero_identificacion = data.get('numero_identificacion')
        identificacion = data.get('identificacion')

        # Verificar si ya existe un Cliente con el mismo número de identificación o identificación.
        if Cuenta.objects.filter(numero_identificacion=numero_identificacion, identificacion=identificacion).exists():
            raise serializers.ValidationError("Ya existe una cuenta con este número y tipo de identificación.")

        return data
            
    def to_representation(self, instance):
        return {
            'id': instance.id,  
            'numero_identificacion': instance.numero_identificacion,          
            'nombre': instance.nombre,        
            'celular': instance.celular,
            'correo': instance.correo,
            'identificacion_id': instance.identificacion_id,
            'identificacion_nombre': instance.identificacion.nombre,
            'ciudad_id': instance.ciudad_id,
            'ciudad_nombre': instance.ciudad.nombre,        
        }        