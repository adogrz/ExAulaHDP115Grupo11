from django.forms import ModelForm
from .models import CanastaBasicaMensual


class CanastaBasicaMensualForm(ModelForm):
    class Meta:
        model = CanastaBasicaMensual
        fields = ['precio']
