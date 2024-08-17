from django import forms
from .models import Pais, Paquete_Turistico, Locacion_Turistica

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ('nombre','estado_pais')
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre del País',
                    'autofocus': True,
                    'class': 'form-control'
                }
            ),
            'estado_pais': forms.TextInput(
                attrs={
                    'placeholder': 'Estado del País',
                    'class': 'form-control'
                }
            )
        }
        
        
class Locacion_TuristicaForm(forms.ModelForm):
    
    class Meta:
        model = Locacion_Turistica
        fields = ("nombre_locacion","pais")
        widgets = {
            'nombre_locacion': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de la Locación',
                    'class': 'form-control'
                }
            ),
            'pais': forms.Select(
                attrs={
                    'placeholder': 'País a visitar',
                    'class': 'form-control'
                }
            ),
            'nombre_locacion': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de la Locación',
                    'class': 'form-control'
                }
            ),
        }
        

class Paquete_TuristicoForm(forms.ModelForm):
    
    class Meta:
        model = Paquete_Turistico
        fields = ("locacion_turistica","actividades","estancia","precio","tiempo_estancia","calificacion","imagen_paquete","fecha_entrada","fecha_salida")
        widgets = {
            'locacion_turistica': forms.Select(
                attrs={
                    'placeholder': 'Locación Turística',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'actividades': forms.Textarea(
                attrs={
                    'placeholder': 'Actividades Predefinidas en el Paquete Turístico',
                    'class': 'form-control',
                    'rows': 3,
                    'cols': 3,
                    'autocomplete': 'off'
                }
            ),
            'estancia': forms.TextInput(
                attrs={
                    'placeholder': 'Estancia',
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
            'tiempo_estancia': forms.NumberInput(
                attrs={
                    'placeholder': 'Tiempo de Estancia',
                    'class': 'form-control',
                    'autocomplete': 'off'
                },
            ),
            'calificacion': forms.NumberInput(
                attrs={
                    'placeholder': 'Calificación',
                    'class': 'form-control',
                    'autocomplete': 'off'
                },
            ),
            'imagen_paquete': forms.FileInput(
                attrs={
                    'placeholder': 'Imagen',
                    'class': 'form-control',
                    'autocomplete': 'off'
                },
            ),
            'fecha_entrada': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'placeholder': 'Entrada',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'fecha_salida': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'placeholder': 'Salida',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
        }

