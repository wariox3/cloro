from django.db import models
from cliente.models.pais import Pais

class Estado(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        db_table = "estado"