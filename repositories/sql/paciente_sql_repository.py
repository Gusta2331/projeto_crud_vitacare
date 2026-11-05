import sqlite3
from models.paciente import Paciente

class PacienteSQLRepository:
    def __init__(self, conn_func):
        self.get_conn = conn_func
        
    def save(self, paciente: Paciente) -> Paciente:
        conn = self.get_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO paciente (nome, cpf, data_nascimento, telefone) VALUES (?, ?, ?, ?)",
                (paciente.nome, paciente.cpf, paciente.data_nascimento, paciente.telefone)
            )
            conn.commit()
            paciente.id_paciente = cursor.lastrowid
            return paciente
        finally:
            conn.close()
    
    def get_all(self) -> list:
        conn = self.get_conn()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_paciente, nome, cpf, data_nascimento, telefone FROM paciente")
            rows = cursor.fetchall()
            return [
                Paciente(r["nome"], r["cpf"], r["data_nascimento"], r["telefone"], r["id_paciente"])
                for r in rows
            ]
        finally:
            conn.close()
    
    def find_by_id(self, id_paciente: int) -> Paciente:
        conn = self.get_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_paciente, nome, cpf, data_nascimento, telefone FROM paciente WHERE id_paciente = ?",
                (id_paciente,)
            )
            row = cursor.fetchone()
            if row:
                return Paciente(row["nome"], row["cpf"], row["data_nascimento"], row["telefone"], row["id_paciente"])
            return None
        finally:
            conn.close()
    
    def update(self, paciente: Paciente) -> bool:
        conn = self.get_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE paciente SET nome = ?, cpf = ?, data_nascimento = ?, telefone = ? WHERE id_paciente = ?",
                (paciente.nome, paciente.cpf, paciente.data_nascimento, paciente.telefone, paciente.id_paciente)
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    def delete(self, id_paciente: int) -> bool:
        conn = self.get_conn()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM paciente WHERE id_paciente = ?", (id_paciente,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()