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
    def guardar_en_json(cls, ruta, archivo):
        rutas = cls.from_json(archivo)
        rutas.append(ruta.to_json())
        with open(archivo, "w") as f:
            json.dump(rutas, f, indent=4, default=lambda x: x.to_json())
            
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
        # Cargar las rutas desde el archivo JSON
        rutas = self.from_json("data/rutaVisita.json")

        # Mostrar la lista de rutas disponibles
        print("Rutas Disponibles:")
        for ruta in rutas:
            print(f"ID: {ruta.id}, Nombre: {ruta.nombre}, Destinos: {ruta.destinos_id}")

        # Solicitar al usuario el ID de la ruta que desea modificar
        id_ruta_modificar = int(input("Ingrese el ID de la ruta a la que desea agregar el destino: "))

        # Encontrar la ruta por su ID
        ruta_encontrada = self.encontrar_cosa_por_id(rutas, id_ruta_modificar)

        if ruta_encontrada:
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
                ruta_encontrada.destinos_id.append(id_destino_agregar)

                # Guardar los cambios en las rutas (lista de rutas actualizada) en el archivo JSON
                with open("data/rutaVisita.json", "w") as f:
                    # Convertir las rutas actualizadas a JSON y guardar todo el contenido
                    json.dump([ruta.to_json() for ruta in rutas], f, indent=4)

                print("Destino agregado a la ruta exitosamente.")
            else:
                print(f"Destino con ID {id_destino_agregar} no encontrado.")
        else:
            print(f"Ruta con ID {id_ruta_modificar} no encontrada.")
            
            
    def eliminar_destino_de_ruta(self):
        # Cargar todas las rutas desde el archivo JSON
        rutas = self.from_json("data/rutaVisita.json")

        # Mostrar la lista actual de destinos en la ruta
        print("Destinos en la Ruta:")
        for destino_id in self.destinos_id:
            print(f"ID de Destino: {destino_id}")

        # Solicitar al usuario el ID del destino que desea eliminar de la ruta
        id_destino_eliminar = int(input("Ingrese el ID del destino que desea eliminar de la ruta: "))

        # Encontrar la ruta por su ID
        ruta_encontrada = self.encontrar_cosa_por_id(rutas, self.id)

        if ruta_encontrada:
            # Verificar si el destino con el ID proporcionado está en la lista de la ruta encontrada
            if id_destino_eliminar in ruta_encontrada.destinos_id:
                # Eliminar el ID del destino de la lista de destinos de la ruta
                ruta_encontrada.destinos_id.remove(id_destino_eliminar)

                # Guardar los cambios en las rutas (lista de rutas actualizada) en el archivo JSON
                with open("data/rutaVisita.json", "w") as f:
                    # Convertir las rutas actualizadas a JSON y guardar todo el contenido
                    json.dump([ruta.to_json() for ruta in rutas], f, indent=4)

                print("Destino eliminado de la ruta exitosamente.")
            else:
                print(f"Destino con ID {id_destino_eliminar} no encontrado en la ruta.")
        else:
            print(f"Ruta con ID {self.id} no encontrada.")