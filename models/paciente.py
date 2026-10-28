class Paciente:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, telefone: str, id_paciente: int = None):
        self.id_paciente = id_paciente
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        
    def to_dict(self):
        return {
            "id_paciente": self.id_paciente,
            "nome": self.nome,
            "cpf": self.cpf,
            "data_nascimento": self.data_nascimento,
            "telefone": self.telefone
        }