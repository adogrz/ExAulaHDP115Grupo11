import decimal
from django import forms
from .models import CanastaBasicaMensual


class CanastaBasicaMensualForm(forms.ModelForm):
    class Meta:
        model = CanastaBasicaMensual
        fields = ['precio']

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < decimal.Decimal('0'):
            self.add_error('precio', 'El precio debe ser mayor a cero')
        return precio

    def __init__(self, *args, **kwargs):
        canasta_basica_mensual_instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        self.fields['precio'].error_messages = {
            'invalid': 'Ingrese un precio válido. Ejemplo: 123.45',
            'min_value': 'El precio debe ser mayor a 0',
            'max_value': 'El precio no debe ser mayor a 999999',
        }
        if canasta_basica_mensual_instance:
            self.initial['precio'] = canasta_basica_mensual_instance.precio
