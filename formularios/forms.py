from django import forms
from .models import Usuario, Promociones, Producto

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'edad')