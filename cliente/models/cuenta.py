from django.db import models
from cliente.models.identificacion import Identificacion
from cliente.models.ciudad import Ciudad

class Cuenta(models.Model):
    numero_identificacion = models.CharField(max_length=20)
    nombre = models.CharField(max_length=200)
    celular = models.CharField(max_length=50)
    correo = models.EmailField(max_length = 255)
    identificacion = models.ForeignKey(Identificacion, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    class Meta:
        db_table = "cuenta"  