import sqlite3
from models.paciente import Paciente

class PacienteSQLRepository:
    def __init__(self, conn_func):
        self.get_conn = conn_func
        
    def save(self, paciente: Paciente) -> Paciente:
        conn = self.get_conn()
            try:
                cursor