from django import forms
from .models import Vuelo

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ('destino','fecha_salida','precio','aerolinea','imagen_vuelo')
        widgets = {
            'destino': forms.Select(
                attrs={
                    'placeholder': 'País a visitar',
                    'class': 'form-control'
                }
            ),
            'fecha_salida': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'placeholder': 'Fecha Salida',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'placeholder': 'Precio',
                    'class': 'form-control',
                    'autocomplete': 'off'
                },
            ),
            'aerolinea': forms.Select(
                attrs={
                    'placeholder': 'País a visitar',
                    'class': 'form-control'
                }
            ),
            'imagen_vuelo': forms.FileInput(
                attrs={
                    'placeholder': 'Imagen',
                    'class': 'form-control',
                    'autocomplete': 'off'
                },
            )
        }