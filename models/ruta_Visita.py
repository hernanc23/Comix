from models.destino_Culinario import destinoCulinario
import json
class rutaVisita:
    def __init__(self, id: int, nombre: str, destinos_id: list[int]):
        self.id = id
        self.nombre = nombre
        self.destinos_id = destinos_id
    
    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "destinos_id": self.destinos_id}
    
    
    @classmethod
    def from_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**ruta) for ruta in data]
    
    def mostrar_detalles(self):
        print("detalles de su ruta:")
        print(f"ID: {self.id}")
        print(f"Nombre de la ruta: {self.nombre}")
        print(f"Destinos: {self.destinos_id}")
        self.obtener_detalles_destinos("data/destinoCulinario.json")
        
        
    @classmethod        
    def guardar_en_json(cls, destino, archivo):
        destinos = cls.from_json(archivo)
        destinos.append(destino.to_json())
        with open(archivo, "w") as f:
            json.dump(destinos, f, indent=4, default=lambda x: x.to_json())
            
    @classmethod
    def agregar_ruta(cls, archivo):
        id_nuevo= int(input("ingrese id nuevo: "))
        nombre_nuevo= input("ingrese nombre de ruta: ")
        destinos_nuevos= [0]
        nueva_ruta= cls(
            id=id_nuevo,
            nombre=nombre_nuevo,
            destinos_id=destinos_nuevos
        )
        cls.guardar_en_json(nueva_ruta,archivo)
        print("Ruta creada")
        
    def encontrar_cosa_por_id(self, cosas, cosa_id):
        for cosa in cosas:
            if cosa.id == cosa_id:
                return cosa
        return None
    
    def obtener_detalles_destinos(self, archivo_destinos):
        # Obtener los IDs de destino basados en las rutas en el historial
        ids_destinos = self.destinos_id

        # Cargar los destinos desde el archivo JSON
        destinos = destinoCulinario.from_json(archivo_destinos)

        # Buscar y devolver los detalles de los destinos correspondientes a los IDs
        detalles_destinos = []
        for destino_id in ids_destinos:
            destino_encontrado = self.encontrar_cosa_por_id(destinos, destino_id)
            if destino_encontrado:
                detalles_destinos.append(destino_encontrado.mostrar_detalles())

        return detalles_destinos
    
    
    def modificar_ruta(self, archivo):
        # Cargar las rutas desde el archivo JSON
        rutas = self.from_json(archivo)

        # Solicitar al usuario el ID de la ruta a modificar
        id_ruta_modificar = int(input("Ingrese el ID de la ruta que desea modificar: "))

        # Encontrar la ruta por su ID
        ruta_encontrada = self.encontrar_cosa_por_id(rutas, id_ruta_modificar)

        if ruta_encontrada:
            # Solicitar al usuario las modificaciones deseadas
            nuevo_nombre = input("Ingrese el nuevo nombre de la ruta: ")

            # Actualizar los detalles de la ruta encontrada
            ruta_encontrada.nombre = nuevo_nombre

            # Guardar las rutas actualizadas en el archivo JSON
            with open(archivo, "w") as f:
                json.dump(rutas, f, indent=4, default=lambda x: x.to_json())

            print("Ruta modificada exitosamente.")
        else:
            print(f"Ruta con ID {id_ruta_modificar} no encontrada.")
            
            
    def agregar_destino_a_ruta(self, archivo_destinos):
        # Cargar los destinos desde el archivo JSON
        destinos = destinoCulinario.from_json(archivo_destinos)

        # Mostrar la lista de destinos disponibles
        print("Destinos Disponibles:")
        for destino in destinos:
            print(f"ID: {destino.id}, Nombre: {destino.nombre}")

        # Solicitar al usuario el ID del destino que desea agregar a la ruta
        id_destino_agregar = int(input("Ingrese el ID del destino que desea agregar a la ruta: "))

        # Verificar si el destino con el ID proporcionado existe
        destino_encontrado = self.encontrar_cosa_por_id(destinos, id_destino_agregar)
        if destino_encontrado:
            # Agregar el ID del destino a la lista de destinos de la ruta
            self.destinos_id.append(id_destino_agregar)

            # Guardar los cambios en la ruta (lista de destinos actualizada) en el archivo JSON
            with open("ruta_archivo_rutas.json", "w") as f:
                 json.dump(self.destinos_id, f, indent=4)

            print("Destino agregado a la ruta exitosamente.")
        else:
            print(f"Destino con ID {id_destino_agregar} no encontrado.")