class CarroCompra:

    # Manejo de sesion:
    # Constructor
    def __init__(self, request):
        self.request=request #Queda alamacenada dentro de la variable request, la peticion (ruquest)
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={} #Cuando se inicia el carro de la compra, construye un diccionario vacio
        #else:
        self.carro=carro

    #Funcion agregar productos
    def agregar(self, producto):
        #Agregamos un producto al carro
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                #"imagen": producto.imagen.url
            }
        #Si lo encuentra le suma uno mas
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break #Para que no sigua avanzando en la lista
        self.guardar_carro() #Para actualizar la sesion

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    #Funcion eliminar producto (elimina el total de cantidades)
    def eliminar(self,producto):
        #Primero almacenamos el id del producto para poder manejarlo
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    #Funcion para eliminar una unidad de un producto
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"] = float(value["precio"]) - producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break #Para que no sigua avanzando en la lista
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
