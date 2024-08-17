from django import forms
from .models import Reserva_Paquete, Reserva_Vuelo

class Reserva_Paquete_Form(forms.ModelForm):
    class Meta:
        model = Reserva_Paquete
        fields = ('nombre_paquete','user','cancelada','aceptada')
        widgets = {
            'nombre_paquete': forms.Select(
                attrs= {
                    'placeholder': 'Nombre Paquete',
                    'class': 'form-control'
                }
            ),
            'user': forms.Select(
                attrs= {
                    'placeholder': 'Usuario',
                    'class': 'form-control'
                }
            ),
            'cancelada': forms.CheckboxInput(
                attrs= {
                    'class': 'form-check-input',
                    'type': 'checkbox'
                }
            ),
            'aceptada': forms.CheckboxInput(
                attrs= {
                    'class': 'form-check-input',
                    'type': 'checkbox'
                }
            ),
        }
        

class Reserva_Vuelo_Form(forms.ModelForm):
    class Meta:
        model = Reserva_Vuelo
        fields = ('vuelo','user','cancelada','aceptada')
        widgets = {
            'vuelo': forms.Select(
                attrs= {
                    'placeholder': 'Vuelo',
                    'class': 'form-control'
                }
            ),
            'user': forms.Select(
                attrs= {
                    'placeholder': 'Usuario',
                    'class': 'form-control'
                }
            ),
            'cancelada': forms.CheckboxInput(
                attrs= {
                    'class': 'form-check-input',
                    'type': 'checkbox'
                }
            ),
            'aceptada': forms.CheckboxInput(
                attrs= {
                    'class': 'form-check-input',
                    'type': 'checkbox'
                }
            ),
        }

class SelectForm(forms.Form):
    tipo_reserva={
    ('Reservas en espera','Reservas en espera'),
    ('Reservas canceladas','Reservas canceladas'),
    ('Reservas aceptadas','Reservas aceptadas')
} 
    Filtrado_Reserva = forms.ChoiceField(choices=tipo_reserva, widget=
        forms.Select(
            attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    
                }
        ), required=True
    )