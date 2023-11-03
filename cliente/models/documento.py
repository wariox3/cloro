from django.db import models
from cliente.models.cuenta import Cuenta
from cliente.models.documento_clase import DocumentoClase

class Documento(models.Model):
    prefijo = models.CharField(max_length=20)
    numero = models.IntegerField()    
    fecha = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    documento_clase = models.ForeignKey(DocumentoClase, on_delete=models.CASCADE)

    class Meta:
        db_table = "documento"  