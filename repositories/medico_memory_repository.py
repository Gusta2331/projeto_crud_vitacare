from models.medico import Medico


class MedicoMemoryRepository:
    def __init__(self):
        self.medicos = {}
        self.proximo_id = 1

    def save(self, medico: Medico) -> Medico:
        for medico_existente in self.medicos.values():
            if medico_existente.crm == medico.crm:
                raise ValueError("Já existe um médico com esse CRM.")

        medico.id_medico = self.proximo_id
        self.medicos[self.proximo_id] = medico
        self.proximo_id += 1

        return medico

    def get_all(self) -> list:
        return list(self.medicos.values())

    def find_by_id(self, id_medico: int) -> Medico:
        return self.medicos.get(id_medico)

    def update(self, medico: Medico) -> bool:
        if medico.id_medico not in self.medicos:
            return False

        for medico_existente in self.medicos.values():
            if (
                medico_existente.crm == medico.crm
                and medico_existente.id_medico != medico.id_medico
            ):
                raise ValueError("Já existe um médico com esse CRM.")

        self.medicos[medico.id_medico] = medico
        return True

    def delete(self, id_medico: int) -> bool:
        if id_medico not in self.medicos:
            return False

        del self.medicos[id_medico]
        return True