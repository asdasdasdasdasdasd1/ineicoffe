from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView, ListView, DetailView
from .models import Reserva
from .forms import ReservaForm

# Create your views here.


#reverse_lazy es para url fijas reverse es para url dinámicas
class ReservaView(FormView):
    template_name = 'reservas/crea-reserva.html'
    form_class = ReservaForm
    #success_url = get_success_url(Reserva.codRes)

    def get_success_url(self):
        return reverse('reserva:detalle',{"pk":self.detalle_reserva})


class DetalleView(DetailView):
    model = Reserva
    template_name = 'reservas/detalle-reserva.html'