import json
class review:
    def __init__ (self, id: int, id_destino: int, id_usuario: int, calificacion: int, comentario: str, animo: str):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
        
    def to_json(self):
        return { "id": self.id, "id_destino": self.id_destino, "id_usuario": self.id_usuario, "calificacion": self.calificacion, "comentario": self.comentario, "animo": self.animo}
    
    @classmethod
    def from_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**reseña) for reseña in data]
    
    @classmethod        
    def guardar_en_json(cls, reseña, archivo):
        reseñas = cls.from_json(archivo)
        reseñas.append(reseña.to_json())
        with open(archivo, "w") as f:
            json.dump(reseñas, f, indent=4, default=lambda x: x.to_json())
   
    @classmethod   
    def crear_review(cls, archivo):
        id_nueva= int(input("Elige nueva id: "))
        id_destinoE= int(input("Elige el destino por id: "))
        id_usuarioE= int(input("escribe tu id: "))
        nueva_calificacion= int(("califica del 1 al 5: "))
        comentario_nuevo=input("escribe aqui un comentario: ")
        animo_nuevo=("escoje animo: positivo o negativo: ")
        
        nueva_review=cls(
            id=id_nueva,
            id_destino=id_destinoE,
            id_usuario=id_usuarioE,
            calififiacion=nueva_calificacion,
            comentario= comentario_nuevo,
            animo=animo_nuevo
            
        )
        cls.guardar_en_json(nueva_review, archivo)
        print("Nueva review agregado exitosamente.")
        
        
    @classmethod   
    def ver_review(cls, reseña):
         if reseña:
        
            print("Detalles de la reseña:")
            print(f"ID: {reseña.id}")
            print(f"ID_destino: {reseña.id_destino}")
            print(f"ID_usuario: {reseña.id_usuario}")
            print(f"calififiacion: {reseña.calificacion}")
            print(f"comentario: {reseña.comentario}")
            print(f"animo: {reseña.animo}")
           
         else:
            print("Reseña no encontrado")
        
  