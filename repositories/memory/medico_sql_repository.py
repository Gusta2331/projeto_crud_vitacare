
import sqlite3

from models.medico import Medico


class MedicoSqlRepository:
    def __init__(self, db_path: str = "vitacare.db"):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS medico (
                id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                crm TEXT NOT NULL UNIQUE,
                especialidade TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """

        with self.connection:
            self.connection.execute(sql)

    def save(self, medico: Medico) -> Medico:
        sql = """
            INSERT INTO medico (
                nome,
                crm,
                especialidade,
                telefone
            )
            VALUES (?, ?, ?, ?)
        """

        with self.connection:
            cursor = self.connection.execute(
                sql,
                (
                    medico.nome,
                    medico.crm,
                    medico.especialidade,
                    medico.telefone
                )
            )

            medico.id_medico = cursor.lastrowid

        return medico

    def get_all(self) -> list[Medico]:
        sql = """
            SELECT
                id_medico,
                nome,
                crm,
                especialidade,
                telefone
            FROM medico
            ORDER BY id_medico
        """

        cursor = self.connection.execute(sql)
        rows = cursor.fetchall()

        return [
            Medico(
                id_medico=row["id_medico"],
                nome=row["nome"],
                crm=row["crm"],
                especialidade=row["especialidade"],
                telefone=row["telefone"]
            )
            for row in rows
        ]

    def find_by_id(self, id_medico: int) -> Medico | None:
        sql = """
            SELECT
                id_medico,
                nome,
                crm,
                especialidade,
                telefone
            FROM medico
            WHERE id_medico = ?
        """

        cursor = self.connection.execute(sql, (id_medico,))
        row = cursor.fetchone()

        if row is None:
            return None

        return Medico(
            id_medico=row["id_medico"],
            nome=row["nome"],
            crm=row["crm"],
            especialidade=row["especialidade"],
            telefone=row["telefone"]
        )

    def update(self, medico: Medico) -> bool:
        sql = """
            UPDATE medico
            SET
                nome = ?,
                crm = ?,
                especialidade = ?,
                telefone = ?
            WHERE id_medico = ?
        """

        with self.connection:
            cursor = self.connection.execute(
                sql,
                (
                    medico.nome,
                    medico.crm,
                    medico.especialidade,
                    medico.telefone,
                    medico.id_medico
                )
            )

        return cursor.rowcount > 0

    def delete(self, id_medico: int) -> bool:
        sql = """
            DELETE FROM medico
            WHERE id_medico = ?
        """

        with self.connection:
            cursor = self.connection.execute(
                sql,
                (id_medico,)
            )

        return cursor.rowcount > 0

    def close(self) -> None:
        self.connection.close()
