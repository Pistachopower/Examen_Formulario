from django import forms
from .models import Usuario, Promociones, Producto

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'edad')
        
        
class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'edad']
        help_texts = {
            "nombre": ("200 caracteres como máximo"),
        }
        
    
    def clean(self):

        super().clean()

        nombre = self.cleaned_data.get('nombre')
        edad = self.cleaned_data.get('edad')

   
        usuarioNombre = Usuario.objects.filter(nombre=nombre).first()
        if(not usuarioNombre is None
           ):
             if(not self.instance is None and usuarioNombre.id == self.instance.id):
                 pass
             else:
                self.add_error('nombre','Ya existe')

            
            
        #Siempre devolvemos el conjunto de datos.
        return self.cleaned_data