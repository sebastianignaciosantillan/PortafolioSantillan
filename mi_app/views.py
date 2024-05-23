# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Contacto

def index(request):
    mensaje_exitoso = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            asunto = form.cleaned_data['tema']
            consulta = form.cleaned_data['mensaje']

            # Enviar correo electrónico
            email_from = settings.EMAIL_HOST_USER
            destinatario = ["sebastianignaciosantillan@gmail.com"]
            send_mail(asunto, consulta, email_from, destinatario)

            # Guardar el formulario en la base de datos
            contacto = Contacto(
                nombre=nombre,
                email=email,
                telefono=telefono,
                asunto=asunto,
                consulta=consulta
            )
            contacto.save()
            mensaje_exitoso = True
            form = ContactForm()  # Limpiar el formulario
            return redirect("Index")
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'mensaje_exitoso': mensaje_exitoso})

