from models.review import review
from models.ruta_Visita import rutaVisita
from models.destino_Culinario import destinoCulinario
import json
class usuario:
    def __init__(self, nombre_usuario: str , contrasena: str, id: int, nombre: str, apellido: str, historial_rutas: list[int]):
        self.nombre_usuario= nombre_usuario
        self.contrasena=contrasena
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas
        
    def to_json(self):
        
        return {"nombre_usuario":self.nombre_usuario,"contrasena":self.contrasena, "id": self.id, "nombre": self.nombre, "apellido": self.apellido, "historial_rutas": self.historial_rutas}
    
    @classmethod
    def from_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**usuario) for usuario in data]
    
    @classmethod        
    def guardar_en_json(cls, usuario, archivo):
        usuarios = cls.from_json(archivo)
        usuarios.append(usuario.to_json())
        with open(archivo, "w") as f:
            json.dump(usuarios, f, indent=4, default=lambda x: x.to_json())
            
    
    @classmethod 
    def crear_cuenta(cls, archivo):
        print("Bienvenido vamos a crear su cuenta:")
        while True:
             nombreUsuario_nuevo = input("Ingrese el nombre del nuevo usuario: ")
             es_repetido = usuario.verificar_nombre_repetido(nombreUsuario_nuevo, "data/usuario.json")
    
             if es_repetido:
                 print(f"El nombre '{nombreUsuario_nuevo}' ya está siendo utilizado por otro usuario.")
             else:
                 print(f"El nombre '{nombreUsuario_nuevo}' no está repetido y puede ser utilizado.")
                 break
        contrasena_nuevo = input ("Cree contraseña por favor: ")
        id_nuevo = int(input("Ingrese el ID del nuevo usuario: "))
        nombre_nuevo = input("Ingrese su nombre: ")
        apellido_nuevo = input("Ingrese su apellido: ")
        historial_nuevo = [0]
        

        nuevo_usuario = cls(
            nombre_usuario= nombreUsuario_nuevo,
            contrasena= contrasena_nuevo,
            id=id_nuevo,
            nombre=nombre_nuevo,
            apellido=apellido_nuevo,
            historial_rutas=historial_nuevo
        )

        cls.guardar_en_json(nuevo_usuario, archivo)

        print("Cuenta creada exitosamente.")
    
    
    @classmethod
    def verificar_nombre_repetido(cls, nombre, archivo):
        usuarios = cls.from_json(archivo)
        nombres_existentes = [usuario.nombre_usuario.lower() for usuario in usuarios]
        return nombre.lower() in nombres_existentes
    
    @classmethod
    def verificar_clave(cls, clave, archivo):
        usuarios = cls.from_json(archivo)
        nombres_existentes = [usuario.contrasena.lower() for usuario in usuarios]
        return clave.lower() in nombres_existentes
    
    @classmethod
    def login(self, archivo):
        while True:
            usuario_log = input("Escribe tu usuario: ")
            veri = self.verificar_nombre_repetido(usuario_log, archivo)
            if veri:
                print(f"El nombre '{usuario_log}' ha sido introducido correctamente.")
                break
            else:
                print(f"El nombre '{usuario_log}' no es correcto.")

        while True:
            clave_log = input("Escribe tu clave: ")
            passw = self.verificar_clave(clave_log, archivo)
            if passw:
                print(f"La clave '{clave_log}' ha sido introducida correctamente.")
                return True  # Devuelve True si el inicio de sesión es exitoso
            else:
                print(f"La clave '{clave_log}' no es correcta.")
                return False  # Devuelve False si el inicio de sesión falla

    @classmethod
    def mostrar_detalles(cls, usuario):
            
      print("Datos del usuario:")
      print(f"Nombre de usuario: {usuario.nombre_usuario}")
      print(f"Contraseña: {usuario.contrasena}")
      print(f"ID: {usuario.id}")
      print(f"Nombre: {usuario.nombre}")
      print(f"Apellido: {usuario.apellido}")
      print(f"Historial de rutas: {usuario.historial_rutas}")
      
   
    def ver_reviews_usuario(self, archivo_reviews):
        reviews = review.from_json(archivo_reviews)
        user_reviews = [reseña for reseña in reviews if reseña.id_usuario == self.id]
        
        if user_reviews:
            print(f"Reviews del usuario '{self.nombre_usuario}':")
            for reseña in user_reviews:
                review.ver_review(reseña)
        else:
            print(f"El usuario '{self.nombre_usuario}' no tiene reseñas.")    
    
        
    def buscar_rutas_en_historial(self, archivo_rutas):
        # Cargar las rutas desde el archivo JSON
        rutas = rutaVisita.from_json(archivo_rutas)
        
        # Obtener el historial de rutas del usuario
        historial_rutas = self.historial_rutas
        
        # Buscar y devolver las rutas en el historial
        rutas_en_historial = []
        for ruta_id in historial_rutas:
            ruta_encontrada = self.encontrar_cosa_por_id(rutas, ruta_id)
            if ruta_encontrada:
                rutas_en_historial.append(ruta_encontrada)
        
        return rutas_en_historial 
    
    def encontrar_cosa_por_id(self, cosas, cosa_id):
        for cosa in cosas:
            if cosa.id == cosa_id:
                return cosa
        return None
        
    def mostrar_detalles_rutas_en_historial(self, archivo_rutas):
        # Buscar las rutas en el historial del usuario
        rutas_en_historial = self.buscar_rutas_en_historial(archivo_rutas)
        
        # Mostrar los detalles de cada ruta encontrada
        for ruta_en_historial in rutas_en_historial:
            ruta_en_historial.mostrar_detalles()
        
            
    def ver_IDSdestinos(self,archivo_rutas):
        misRutas=self.buscar_rutas_en_historial(archivo_rutas)
        lugares=[]
        for miruta in misRutas:
            lugares.extend(miruta.destinos)
        conj_lugares=set(lugares)
        lugares_sin_repetidos= list(conj_lugares)
        return lugares_sin_repetidos
    
    
    def obtener_detalles_destinos(self, archivo_rutas, archivo_destinos):
        # Obtener los IDs de destino basados en las rutas en el historial
        ids_destinos = self.ver_IDSdestinos(archivo_rutas)

        # Cargar los destinos desde el archivo JSON
        destinos = destinoCulinario.from_json(archivo_destinos)

        # Buscar y devolver los detalles de los destinos correspondientes a los IDs
        detalles_destinos = []
        for destino_id in ids_destinos:
            destino_encontrado = self.encontrar_cosa_por_id(destinos, destino_id)
            if destino_encontrado:
                detalles_destinos.append(destino_encontrado.mostrar_detalles())

        return detalles_destinos