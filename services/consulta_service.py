class ConsultaService:

    def __init__(self, consulta_repo):
        self.consulta_repo = consulta_repo

    def get_atendimentos_faturamento_por_medico(self):
        """
        Solicita ao repositório o relatório de
        atendimentos e faturamento por médico.
        """

        return self.consulta_repo.get_atendimentos_faturamento_por_medico()

    def get_media_valor_por_especialidade(self):
        """
        Solicita ao repositório o relatório de
        média de valores por especialidade.
        """

        return self.consulta_repo.get_media_valor_por_especialidade()