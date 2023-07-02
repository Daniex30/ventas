from django import forms

from .models import Categoria, Marca, Estado, Producto


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = [
            'nombre',
        ]
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'id':'nombre',
                'required': 'True',
            }
        )

class MarcaForm(forms.ModelForm):

    class Meta:

        model = Marca
        fields = [
                'nombre',
        ]
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'id':'nombre',
                'required': 'True',
                }
            )
        
class EstadoForm(forms.ModelForm):

    class Meta:

        model = Estado
        fields = [
                'nombre',
        ]
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'id':'nombre',
                'required': 'True',
                }
            )

class ProductoForm(forms.ModelForm):

    codigo = forms.CharField(
    required=True,
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'id':'codigo',
            }
        )
    )

    nombre = forms.CharField(
    required=True,
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'id':'nombre',
            }
        )
    )

    descripcion = forms.CharField(
    widget=forms.Textarea(
        attrs={
                'class': 'form-control',
                'id':'descripcion',
            }
        )
    )

    unidad_medida = forms.CharField(
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'id':'um',
            }
        )
    )

    precio_venta = forms.IntegerField(
    required=True,
    widget=forms.NumberInput(
        attrs={
                'class': 'form-control',
                'id':'precio_venta',
            }
        )
    )
    
    class Meta:
        
        model = Producto
        fields = (
            'codigo',
            'nombre',
            'descripcion',
            'unidad_medida',
            'precio_venta',
            'categoria',
            'marca',
            'estado',
        )


class UpdateProductForm(forms.ModelForm):
    
    codigo = forms.CharField(
    required=True,
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'id':'codigo',
            }
        )
    )

    nombre = forms.CharField(
    required=True,
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'id':'nombre',
            }
        )
    )

    descripcion = forms.CharField(
    widget=forms.Textarea(
        attrs={
                'class': 'form-control',
                'id':'descripcion',
            }
        )
    )

    unidad_medida = forms.CharField(
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'id':'um',
            }
        )
    )

    precio_venta = forms.IntegerField(
    required=True,
    widget=forms.NumberInput(
        attrs={
                'class': 'form-control',
                'id':'precio_venta',
            }
        )
    )
    
    class Meta:
        
        model = Producto
        fields = (
            'codigo',
            'nombre',
            'descripcion',
            'unidad_medida',
            'precio_venta',
            'categoria',
            'marca',
        )

class BlockProductForm(forms.ModelForm):
    codigo = forms.CharField(
    required=True,
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'id':'codigo',
            }
        )
    )

    nombre = forms.CharField(
    required=True,
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'id':'nombre',
            }
        )
    )

    unidad_medida = forms.CharField(
    widget=forms.TextInput(
        attrs={
                'class': 'form-control',
                'id':'um',
            }
        )
    )

    precio_venta = forms.IntegerField(
    required=True,
    widget=forms.NumberInput(
        attrs={
                'class': 'form-control',
                'id':'precio_venta',
            }
        )
    )
    
    class Meta:
        
        model = Producto
        fields = (
            'codigo',
            'nombre',
            'unidad_medida',
            'precio_venta',
            'estado',
        )
