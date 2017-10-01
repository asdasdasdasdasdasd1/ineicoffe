from django import forms
from .models import Reserva


class ReservaForm(forms.Form):
    dni = forms.CharField(max_length=8, min_length=8, required=True)
    ambiente = forms.CharField(max_length=10)

    class Meta:
        model: Reserva
        fields: ('codRes','nomPerRes', 'apePerRes', 'dniPerRes', 'nroPerRes')