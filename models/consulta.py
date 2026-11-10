class Consulta:
    def __init__(
        self,
        id_paciente,
        id_medico,
        data_hora,
        diagnostico,
        valor_consulta,
        id_consulta=None
    ):

        self.id_consulta = id_consulta
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.data_hora = data_hora
        self.diagnostico = diagnostico
        self.valor_consulta = valor_consulta


    def to_dict(self):
        return {
              "id_consulta": self.id_consulta,
            "id_paciente": self.id_paciente,
            "id_medico": self.id_medico,
            "data_hora": self.data_hora,
            "diagnostico": self.diagnostico,
            "valor_consulta": self.valor_consulta
        }