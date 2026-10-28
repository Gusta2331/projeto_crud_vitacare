from models.paciente import Paciente

class PacienteMemoryRepository:
    def __init__(self):
        self.storage = {}
        self.counter = 1

    #Salvar
    def save(self, paciente: Paciente) -> Paciente:
        if paciente.id_paciente is None:
            paciente.id_paciente = self.counter
            self.counter += 1
        self.storage[paciente.id_paciente] = paciente
        return paciente
    
    #listar tudo
    def get_all(self) -> list:
        return list(self.storage.values())
    
    #encontrar por id
    def find_by_id(self, id_paciente: int) -> Paciente:
        return self.storage.get(id_paciente)
    
    #Atualizar
    def update(self, paciente: Paciente) -> bool:
        if paciente.id_paciente in self.storage:
            self.storage[paciente.id_paciente] = paciente
            
    def delete(self, id_paciente: int) -> bool:
        if id_paciente in self.storage:
            del self.storage[id_paciente]
            return True
        return False