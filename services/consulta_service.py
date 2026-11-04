class ConsultaService:

    def __init__(self, consulta_repo):
        self.consulta_repo = consulta_repo

    def get_atendimentos_faturamento_por_medico(self):

        return self.consulta_repo.get_atendimentos_faturamento_por_medico()

    def get_media_valor_por_especialidade(self):
    

        return self.consulta_repo.get_media_valor_por_especialidade()