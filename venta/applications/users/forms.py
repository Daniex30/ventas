from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
    required=True,
    widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'id':'password1',
            }
        )
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id':'password2',
            }
        )
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'username',
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control',
            }
        )
    )
    nombre = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'username',
                'class': 'form-control',
            }
        )
    )
    apellido = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'apellido',
                'class': 'form-control',
            }
        )
    )
    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'nombre',
            'apellido',
            'rol',
        )

    # funcion para validar que las contraseñas son iguales
    def clean_password2(self):
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                  'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        password = self.cleaned_data['password1']
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas son diferentes')
        elif len(password) < 8:
            self.add_error(
                'password2', 'La contraseña ingresada tiene menos de 8 caracteres')
        elif not any(letra_p in letras for letra_p in password):
            self.add_error(
                'password2', 'La contraseña no contiene letras')
        elif not any(numero_p in numeros for numero_p in password):
            self.add_error(
                'password2', 'La contraseña no contiene numeros')

class LoginForm(forms.Form):
    email = forms.CharField(
        label= 'Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )
        
    password = forms.CharField(
        label= 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    def clean(self):

        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('')
        return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label= 'Contraseña actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    password2 = forms.CharField(
        label= 'Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password3 = forms.CharField(
        label= 'Repetir Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    def clean_password3(self):
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                  'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        password = self.cleaned_data['password2']
        if self.cleaned_data['password2'] != self.cleaned_data['password3']:
            self.add_error('password3', 'Las contraseñas son diferentes')
        elif len(password) < 8:
            self.add_error(
                'password3', 'La contraseña ingresada tiene menos de 8 caracteres')
        elif not any(letra_p in letras for letra_p in password):
            self.add_error(
                'password3', 'La contraseña no contiene letras')
        elif not any(numero_p in numeros for numero_p in password):
            self.add_error(
                'password3', 'La contraseña no contiene numeros')
            

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "nombre",
            "apellido",
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }