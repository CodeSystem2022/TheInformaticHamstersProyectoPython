#Aqui armamos la variable para almacenar el monto
# de los productos que se van agregando al carro

def importe_total_carro(request):
    #Esta es la variable
    total=0
    if "carro" in request.session: #La sentencia original era: if request.user.is_authenticated(): #No se puede usar mientras no haya un sistema de autenticacion
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"])
    return {"importe_total_carro": total}

#Para que a la variable importe_total_carro se pueda acceder desde cualquier lado del proyecto
#debemos registrarla en el setting