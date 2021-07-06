from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Producto


class ProductoForm(ModelForm):
    class Meta :
        model=Producto
        fields=['numeroID','nombreCompleto','telefono','categoria','direccion','imagen','email','pais','contrasenna']
        
        labels={
            'numeroID':'ingrese ID',
            'nombreCompleto':'Nombre Completo',
            'telefono':'ingrese telefono',
            'categoria':'seleccione categoria',
            'direccion':'ingrese direccion',
            'imagen':'ingrese logoproveedor',
            'email':'ingrese email',
            'pais':'ingrese pais',
            'contrasenna':'ingrese contraseña'


        }
        
        widgets={
            'numeroID': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'numeroID',
                    'id':'numeroID'


                }
            ),
            'nombreCompleto': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'nombreCompleto',
                    'id':'nombreCompleto'


                }

            ),
            'telefono':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'telefono',
                    'id':'telefono'

                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'categoria'

                }

            ),
            'direccion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'direccion'
                }

            ),
            'imagen':forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen'
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'email'
                }
            ),
            'pais':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'pais'
                }
            ),
            'contrasenna':forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'id':'contrasenna'
                }

            ),
            
           


            


        }