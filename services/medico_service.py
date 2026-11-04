from models.medico import Medico

class MedicoService:
    def __init__(self, repo):
        self.repo = repo
    def validar_medico(self, medico: Medico) -> None:
        if not medico.nome or not medico.nome.strip():
            raise ValueError("O nome do médico é obrigatorio!")

        if not medico.crm or not medico.crm.strip():
            raise ValueError("O CRM do médico é obrigatório.")

        if not medico.especialidade or not medico.especialidade.strip():
             raise ValueError("A especialidade do médico é obrigatória.")

    def save(self, medico: Medico) -> Medico:
        self._validar_medico(medico)
        return self.repo.save(medico)
    
    def get_all(self) -> list:
        return self.repo.get_all()

    def find_by_id(self, id_medico: int) -> Medico:
        return self.repo.find_by_id(id_medico)

    def update(self, medico: Medico) -> bool:
        self._validar_medico(medico)
        return self.repo.update(medico)

    def delete(self, id_medico: int) -> bool:
        return self.repo.delete(id_medico)


        
 