from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {'username': "El nombre de usuario debe ser el número de CUIT asociado a la factura",
                      'password1': None,
                      'password2': None,
                      }
