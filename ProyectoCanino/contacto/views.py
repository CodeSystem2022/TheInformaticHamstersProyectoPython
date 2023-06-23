from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

    #Rescatamos la informacion del formulario y la guardamos en las variables nombre, email y contenido
    if request.method == "POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage(f'Mensaje de usuario", "Usuario: {nombre} - Email: {email} - Mensaje: \n\n {contenido}', "", ["pruebatecnicatura@outlook.com"], reply_to=[email])

            try:
                email.send()
                #Redirigimos la informacion al template contacto
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {"miFormulario":formulario_contacto})