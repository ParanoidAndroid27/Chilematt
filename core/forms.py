from django import forms
from django.forms import inlineformset_factory
from .models import Venta, DetalleVenta
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['codigo_venta', 'cliente', 'fecha_compra']
        

DetalleVentaFormSet = inlineformset_factory(Venta, DetalleVenta, fields=('producto', 'cantidad'))


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user