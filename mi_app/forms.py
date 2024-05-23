from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Tú Nombre',
        'required': 'required'
    }))
    telefono = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'placeholder': 'Número telefónico',
        'required': 'required',
        'type': 'tel'
    }))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Dirección de correo',
        'required': 'required'
    }))
    tema = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Tema',
        'required': 'required'
    }))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Mensaje',
        'required': 'required',
        'cols': 30,
        'rows': 10
    }))
