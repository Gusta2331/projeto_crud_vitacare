class ConsultaMemoryRepository:

    def __init__(self, consultas=None, medicos=None):

        self.consultas = consultas if consultas is not None else {}
        self.medicos = medicos if medicos is not None else {}

    def _obter_valor(self, objeto, atributo, padrao=None):

        if isinstance(objeto, dict):
            return objeto.get(atributo, padrao)

        return getattr(objeto, atributo, padrao)

    def _listar_medicos(self):

        if isinstance(self.medicos, dict):
            return list(self.medicos.values())

        return list(self.medicos)

    def _listar_consultas(self):

        if isinstance(self.consultas, dict):
            return list(self.consultas.values())

        return list(self.consultas)

    def get_atendimentos_faturamento_por_medico(self):
      
        medicos = self._listar_medicos()
        consultas = self._listar_consultas()

        resultados = []

        for medico in medicos:

            id_medico = self._obter_valor(
                medico,
                "id_medico"
            )

            nome = self._obter_valor(
                medico,
                "nome",
                "Médico não identificado"
            )

            quantidade = 0
            faturamento_total = 0

            for consulta in consultas:

                consulta_id_medico = self._obter_valor(
                    consulta,
                    "id_medico"
                )

                if consulta_id_medico == id_medico:

                    quantidade += 1

                    valor = self._obter_valor(
                        consulta,
                        "valor_consulta",
                        0
                    )

                    faturamento_total += float(valor or 0)

            resultados.append({
                "id_medico": id_medico,
                "nome": nome,
                "quantidade": quantidade,
                "faturamento_total": faturamento_total
            })

        resultados.sort(
            key=lambda item: item["nome"]
        )

        return resultados

    def get_media_valor_por_especialidade(self):
       

        medicos = self._listar_medicos()
        consultas = self._listar_consultas()

        especialidades = {}

        for consulta in consultas:

            id_medico = self._obter_valor(
                consulta,
                "id_medico"
            )

            valor = self._obter_valor(
                consulta,
                "valor_consulta"
            )

            if valor is None:
                continue

            for medico in medicos:

                id_medico_cadastrado = self._obter_valor(
                    medico,
                    "id_medico"
                )

                if id_medico == id_medico_cadastrado:

                    especialidade = self._obter_valor(
                        medico,
                        "especialidade"
                    )

                    if not especialidade:
                        break

                    if especialidade not in especialidades:
                        especialidades[especialidade] = []

                    especialidades[especialidade].append(
                        float(valor)
                    )

                    break

        resultados = []

        for especialidade, valores in especialidades.items():

            media = sum(valores) / len(valores)

            resultados.append({
                "especialidade": especialidade,
                "media_valor": media
            })

        resultados.sort(
            key=lambda item: item["especialidade"]
        )

        return resultados