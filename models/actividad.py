import datetime

class actividad:
    def __init__(self, id: int, nombre: str, destino_id: int, hora_inicio: str):
    
        """
        datetime ISO 8601
        """
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio
        
    def to_json():
        pass
    
    @classmethod
    def from_json():
        pass