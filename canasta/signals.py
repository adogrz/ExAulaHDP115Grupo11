from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import CanastaBasicaAnual, CanastaBasicaMensual


@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'canasta':
        anios = [2019, 2020, 2021, 2022, 2023]
        for anio in anios:
            cba = CanastaBasicaAnual.objects.create(
                anio=anio, precio_promedio=0, inflacion=0)
            for _ in range(12):
                CanastaBasicaMensual.objects.create(precio=0, anual=cba)
