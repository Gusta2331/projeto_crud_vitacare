from models.consulta import Consulta

class ConsultaSQLRepository:
    def __init__(self, conexao):
        self.conexao = conexao

    def save(self, consulta):
        cursor = self.conexao.cursor()

        cursor.execute(
            """
            INSERT INTO consulta (
                id_paciente,
                id_medico,
                data_hora,
                diagnostico,
                valor_consulta
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                consulta.id_paciente,
                consulta.id_medico,
                consulta.data_hora,
                consulta.diagnostico,
                consulta.valor_consulta
            )
        )


        self.conexao.commit()

        consulta.id_consulta = cursor.lastrowid

        return consulta


    def find_by_id(self, id_consulta):
        cursor = self.conexao.cursor()

        cursor.execute(
            "SELECT * FROM consulta WHERE id_consulta = ?",
            (id_consulta,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            return None

        return Consulta(
            id_consulta=resultado[0],
            id_paciente=resultado[1],
            id_medico=resultado[2],
            data_hora=resultado[3],
            diagnostico=resultado[4],
            valor_consulta=resultado[5]
        )

    def get_all(self):
        cursor = self.conexao.cursor()

        cursor.execute("SELECT * FROM consulta")

        resultados = cursor.fetchall()

        consultas = []

        for resultado in resultados:
            consulta = Consulta(
            id_consulta=resultado[0],
            id_paciente=resultado[1],
            id_medico=resultado[2],
            data_hora=resultado[3],
            diagnostico=resultado[4],
            valor_consulta=resultado[5]
        )

            consultas.append(consulta)

        return consultas

    def update(self, consulta):
        cursor = self.conexao.cursor()

        cursor.execute(
            """
            UPDATE consulta
            SET id_paciente = ?,
                id_medico = ?,
                data_hora = ?,
                diagnostico = ?,
                valor_consulta = ?
            WHERE id_consulta = ?
            """,
            (
                consulta.id_paciente,
                consulta.id_medico,
                consulta.data_hora,
                consulta.diagnostico,
                consulta.valor_consulta,
                consulta.id_consulta
            )
        )

        self.conexao.commit()

        return cursor.rowcount > 0

    def delete(self, id_consulta):
        cursor = self.conexao.cursor()

        cursor.execute(
            "DELETE FROM consulta WHERE id_consulta = ?",
            (id_consulta,)
        )

        self.conexao.commit()

        return cursor.rowcount > 0
