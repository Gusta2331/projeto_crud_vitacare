class ConsultaSQLRepository:

    def __init__(self, connection):
        self.connection = connection

    def get_atendimentos_faturamento_por_medico(self):
       

        sql = """
            SELECT
                m.id_medico,
                m.nome,
                COUNT(c.id_consulta) AS quantidade,
                COALESCE(SUM(c.valor_consulta), 0) AS faturamento_total
            FROM medico m
            LEFT JOIN consulta c
                ON m.id_medico = c.id_medico
            GROUP BY
                m.id_medico,
                m.nome
            ORDER BY
                m.nome;
        """

        cursor = self.connection.cursor()
        cursor.execute(sql)

        resultados = cursor.fetchall()

        colunas = [
            descricao[0]
            for descricao in cursor.description
        ]

        return [
            dict(zip(colunas, linha))
            for linha in resultados
        ]

    def get_media_valor_por_especialidade(self):
        

        sql = """
            SELECT
                m.especialidade,
                AVG(c.valor_consulta) AS media_valor
            FROM consulta c
            INNER JOIN medico m
                ON c.id_medico = m.id_medico
            GROUP BY
                m.especialidade
            ORDER BY
                m.especialidade;
        """

        cursor = self.connection.cursor()
        cursor.execute(sql)

        resultados = cursor.fetchall()

        colunas = [
            descricao[0]
            for descricao in cursor.description
        ]

        return [
            dict(zip(colunas, linha))
            for linha in resultados
        ]