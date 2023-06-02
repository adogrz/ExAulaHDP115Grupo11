from django.db import models


# Create your models here.


class CanastaBasicaAnual(models.Model):
    anio = models.IntegerField(unique=True)
    precio_promedio = models.DecimalField(
        max_digits=6, decimal_places=2)
    inflacion = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    objects = models.Manager()


class CanastaBasicaMensual(models.Model):
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    anual = models.ForeignKey(
        CanastaBasicaAnual, on_delete=models.CASCADE,
        related_name='canastasBasicasMensuales')
    objects = models.Manager()
