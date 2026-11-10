class ConsultaService:
    def __init__(self, consulta_repo, paciente_repo=None, medico_repo=None):
        self.consulta_repo = consulta_repo
        self.paciente_repo = paciente_repo
        self.medico_repo = medico_repo  

    def validar_valor(self, valor_consulta):
        if valor_consulta < 0:
            raise ValueError("O valor da consulta não pode ser negativo")
        return True

    def validar_paciente(self, id_paciente):
        if self.paciente_repo is None:
            return True
        paciente = self.paciente_repo.find_by_id(id_paciente)
        if paciente is None:
            raise ValueError("Paciente não encontrado")
        return True

    def validar_medico(self, id_medico):
        if self.medico_repo is None:
            return True
        medico = self.medico_repo.find_by_id(id_medico)
        if medico is None:
            raise ValueError("Médico não encontrado")
        return True

    # --- MÉTODOS DE NEGÓCIO E CRUD ---
    def agendar_consulta(self, consulta):
        self.validar_paciente(consulta.id_paciente)
        self.validar_medico(consulta.id_medico)
        self.validar_valor(consulta.valor_consulta)
        return self.consulta_repo.save(consulta)

    def listar_consultas(self):
        return self.consulta_repo.get_all()

    def buscar_consulta(self, id_consulta):
        return self.consulta_repo.find_by_id(id_consulta)

    def atualizar_consulta(self, consulta):
        self.validar_paciente(consulta.id_paciente)
        self.validar_medico(consulta.id_medico)
        self.validar_valor(consulta.valor_consulta)
        return self.consulta_repo.update(consulta)

    def excluir_consulta(self, id_consulta):
        return self.consulta_repo.delete(id_consulta)

    # --- MÉTODOS DE RELATÓRIOS (DA MAIN) ---
    def get_atendimentos_faturamento_por_medico(self):
        return self.consulta_repo.get_atendimentos_faturamento_por_medico()

    def get_media_valor_por_especialidade(self):
        return self.consulta_repo.get_media_valor_por_especialidade()