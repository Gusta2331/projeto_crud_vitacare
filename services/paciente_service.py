from models.paciente import Paciente

class PacienteService:
    def __init__(self, repo):
        self.repo = repo
        
    def register(self, nome: str, cpf: str, data_nascimento: str, telefone: str) -> Paciente:
        if not nome or not nome.strip():
            raise ValueError("O nome do paciente é obrigatório!")
        
        cpf_limpo = cpf.strip().replace(".", "").replace("-", "")
        if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
            raise ValueError("CPF inválido! Deve conter exatamente 11 dígitos numéricos!")
        
        paciente = Paciente(
            nome = nome.strip(),
            cpf = cpf_limpo,
            data_nascimento = data_nascimento.strip(),
            telefone = telefone.strip(),
            id_paciente = id_paciente
        )
        return self.repo.update(paciente)
    
    def deletar(self, id_paciente: int) -> bool:
        self.buscar_por_id(id_paciente)
        return self.repo.delete(id_paciente)