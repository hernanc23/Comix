from models.destino_Culinario import destinoCulinario
import datetime
import json
class actividad:
    def __init__(self, id: int, nombre: str, destino_id: int, hora_inicio: str):
    
        
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = datetime.datetime.fromisoformat(hora_inicio) #datetime ISO 8601
        
    def to_json(self):
        hora_inicio_iso8601 = self.hora_inicio.isoformat()
        return {"id": self.id, "nombre": self.nombre, "destino_id": self.destino_id, "hora_inicio": hora_inicio_iso8601 }
    
    @classmethod
    def from_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**actividad) for actividad in data]
    
    def verDestino_asociado(self,archivo_destino):
        destinos= destinoCulinario.from_json(archivo_destino)#extraigo todos los destinos
        destino_especifico=[destino for destino in destinos if destino.id == self.destino_id]
        
        if destino_especifico:
           
            for destino in destino_especifico:
                print(f"El destino asociado: {destino.nombre}")
        
        
    
    def mostrar_detalles(self):
         print("Detalles de la actividad:")
         print(f"ID: {self.id}")
         print(f"Nombre: {self.nombre}")
         print(f"ID del destino: {self.destino_id}")
         self.verDestino_asociado("data/destinoCulinario.json")
         print(f"Hora de inicio: {self.hora_inicio}")
         
        
        