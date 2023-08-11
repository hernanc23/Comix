import json

class destinoCulinario:
    def __init__(self, id: int, nombre: str, tipo_cocina: str, ingredientes: list[str], precio_minimo: float, precio_maximo: float, popularidad: float, disponibilidad: bool, id_ubicacion: int, imagen: str ):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen
        
    def to_json(self):
        return { "id": self.id, "nombre": self.nombre, "tipo_cocina": self.tipo_cocina, "ingredientes": self.ingredientes, "precio_minimo": self.precio_minimo, "precio_maximo": self.precio_maximo, "popularidad": self.popularidad, "disponibilidad": self.disponibilidad, "id_ubicacion": self.id_ubicacion, "imagen":self.imagen}
    
    @classmethod
    def from_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**destino) for destino in data]
    
    @classmethod
    def buscar_por_nombre(cls, nombre_busqueda, lista_destinos):
        for destino in lista_destinos:
            if destino.nombre == nombre_busqueda:
                return destino
        return None
    
    @classmethod
    def buscar_por_ID(cls, id_busqueda, lista_destinos):
        for destino in lista_destinos:
            if destino.id == id_busqueda:
                return destino
        return None
    
   
    def mostrar_detalles(self):
        
        
         print("Detalles del destino:")
         print(f"ID: {self.id}")
         print(f"Nombre: {self.nombre}")
         print(f"Tipo de Cocina: {self.tipo_cocina}")
         print(f"Ingredientes: {', '.join(self.ingredientes)}")
         print(f"Precio Mínimo: {self.precio_minimo}")
         print(f"Precio Máximo: {self.precio_maximo}")
         print(f"Popularidad: {self.popularidad}")
         print(f"Disponibilidad: {'Disponible' if self.disponibilidad else 'No disponible'}")
         print(f"Ubicación: {self.id_ubicacion}")
         print(f"Imagen: {self.imagen}")
        
            
    @classmethod
    def mostrar_Destinos(cls, destinos):
        print("nuestros destinos disponibles son:")
        for destino in destinos:
            print(f"Nombre: {destino.nombre}")
    
    
    @classmethod        
    def guardar_en_json(cls, destino, archivo):
        destinos = cls.from_json(archivo)
        destinos.append(destino.to_json())
        with open(archivo, "w") as f:
            json.dump(destinos, f, indent=4, default=lambda x: x.to_json())
            
    
    @classmethod 
    def agregar_destino_interactivo(cls, archivo):
        id_nuevo = int(input("Ingrese el ID del nuevo destino: "))
        
        while True:
             nombre_nuevo = input("Ingrese el nombre del nuevo destino: ")
             es_repetido = destinoCulinario.verificar_nombre_repetido(nombre_nuevo, "data/destinoCulinario.json")
    
             if es_repetido:
                 print(f"El nombre '{nombre_nuevo}' ya está siendo utilizado por otro destino.")
             else:
                 print(f"El nombre '{nombre_nuevo}' no está repetido y puede ser utilizado.")
                 break
           
        tipo_cocina_nuevo = input("Ingrese el tipo de cocina del nuevo destino: ")
        ingredientes_nuevo = input("Ingrese los ingredientes del nuevo destino (separados por comas): ").split(',')
        precio_minimo_nuevo = float(input("Ingrese el precio mínimo del nuevo destino: "))
        precio_maximo_nuevo = float(input("Ingrese el precio máximo del nuevo destino: "))
        popularidad_nueva = float(input("Ingrese la popularidad del nuevo destino: "))
        disponibilidad_nueva = int(input("Ingrese la disponibilidad del nuevo destino (0 o 1): "))
        id_ubicacion_nueva = int(input("Ingrese el ID de ubicación del nuevo destino: "))
        imagen_nueva = input("Ingrese el nombre de la imagen del nuevo destino: ")

        nuevo_destino = cls(
            id=id_nuevo,
            nombre=nombre_nuevo,
            tipo_cocina=tipo_cocina_nuevo,
            ingredientes=ingredientes_nuevo,
            precio_minimo=precio_minimo_nuevo,
            precio_maximo=precio_maximo_nuevo,
            popularidad=popularidad_nueva,
            disponibilidad=disponibilidad_nueva,
            id_ubicacion=id_ubicacion_nueva,
            imagen=imagen_nueva
        )

        cls.guardar_en_json(nuevo_destino, archivo)

        print("Nuevo destino agregado exitosamente.")
    
    
    @classmethod
    def verificar_nombre_repetido(cls, nombre, archivo):
        destinos = cls.from_json(archivo)
        nombres_existentes = [destino.nombre.lower() for destino in destinos]
        return nombre.lower() in nombres_existentes
