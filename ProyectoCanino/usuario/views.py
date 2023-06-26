from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class Registro(View):
    #Metodos get para ofrecer el formulario
    def get(self, request):
        #Con esta clase creamos el formulario para crear usuarios
        form=UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})


    #Metodo para enviar los datos a la BD
    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():
            #Con esta instruccion se almacena el usuario en la base de datos
            usuario=form.save()

            #Funcion para que el usuario quede logueado luego que se registra
            login(request, usuario)

            return redirect("Home")
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render(request, "registro/registro.html", {"form": form})

def cerrar_sesion(request):
    logout(request)

    return redirect("Home")

def loguear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contrasena)
            if usuario is not None:
                login(request, usuario)
                return redirect("Home")
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Usuario no valido")
    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})