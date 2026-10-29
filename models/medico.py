class Medico:
    def __init__( self, nome: str, crm: str,especialidade: str, telefone: str, id_medico: int = None):
        
        self.id_medico = id_medico
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
        self.telefone = telefone

    def to_dict(self) -> dict:
        return {
            "id_medico": self.id_medico,
            "nome": self.nome,
            "crm": self.crm,
            "especialidade": self.especialidade,
            "telefone": self.telefone
        }