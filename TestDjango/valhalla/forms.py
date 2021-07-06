from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Producto


class ProductoForm(ModelForm):
    class Meta :
        model=Producto
        fields=['numeroSerie','marca','modelo','categoria','imagen']
        
        labels={
            'numeroSerie':'ingrese numero serie',
            'marca':'ingrese la marca',
            'modelo':'ingrese modelo',
            'categoria':'seleccione categoria',
            'imagen':'ingrese logoproveedor'

        }
        
        widgets={
            'numeroSerie': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'numeroSerie',
                    'id':'numeroSerie'


                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'marca',
                    'id':'marca'


                }

            ),
            'modelo':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'modelo',
                    'id':'modelo'

                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'categoria'

                }

            ),
            'imagen':forms.FileInput(
                 attrs={
                    'class':'form-control',
                    'id':'imagen',
                    'name':'imagen'

                }


            )


        }