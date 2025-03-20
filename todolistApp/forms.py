
from django import forms
from .models import Tickets

class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['title', 'description', 'usuario']

    def save(self, commit=True):
        instancia = super().save(commit=False)
        instancia.status = "Pendiente"  # Asignar el valor por defecto
        if commit:
            instancia.save()
        return instancia    