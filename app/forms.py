from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Si tu modelo se llama CustomUser


class RegistroForm(UserCreationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Guardar el correo electrónico
        user.rol = 'Invitado'  # Asignar el rol 'Invitado' automáticamente
        if commit:
            user.save()  # Guardar el usuario en la base de datos
        return user
