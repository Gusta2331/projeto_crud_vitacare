
import sqlite3
import tempfile
from pathlib import Path

from models.consulta import Consulta
from repositories.sql.consulta_sql_repository import ConsultaSQLRepository
from services.consulta_service import ConsultaService


def executar_testes():
    # Banco temporário para não alterar os dados reais
    with tempfile.TemporaryDirectory() as pasta:
        caminho_banco = Path(pasta) / "teste_vitacare.db"

        conexao = sqlite3.connect(caminho_banco)
        conexao.execute("PRAGMA foreign_keys = ON")

        caminho_schema = (
            Path(__file__).resolve().parents[1]
            / "database"
            / "schema.sql"
        )

        with open(caminho_schema, "r", encoding="utf-8") as arquivo:
            conexao.executescript(arquivo.read())

        # Dados necessários para os testes
        conexao.execute("""
            INSERT INTO paciente
            (nome, cpf, data_nascimento, telefone)
            VALUES ('Paciente Teste 1', '11111111111', '01/01/1990', '74999999999')
        """)

        conexao.execute("""
            INSERT INTO paciente
            (nome, cpf, data_nascimento, telefone)
            VALUES ('Paciente Teste 2', '22222222222', '02/02/1990', '74888888888')
        """)

        conexao.execute("""
            INSERT INTO medico
            (nome, crm, especialidade, telefone)
            VALUES ('Medico Teste 1', 'CRM001', 'Cardiologia', '74777777777')
        """)

        conexao.execute("""
            INSERT INTO medico
            (nome, crm, especialidade, telefone)
            VALUES ('Medico Teste 2', 'CRM002', 'Ortopedia', '74666666666')
        """)

        conexao.commit()

        repositorio = ConsultaSQLRepository(conexao)
        servico = ConsultaService(repositorio)

        # TESTE 1: primeira consulta deve ser aceita
        consulta1 = Consulta(
            id_paciente=1,
            id_medico=1,
            data_hora="20/11/2026 14:00",
            diagnostico="Consulta de rotina",
            valor_consulta=150
        )

        resultado = servico.agendar_consulta(consulta1)

        assert resultado is not None
        assert resultado.id_consulta is not None

        print("PASSOU: primeira consulta cadastrada.")

        # TESTE 2: mesmo médico e mesmo horário deve ser rejeitado
        consulta2 = Consulta(
            id_paciente=2,
            id_medico=1,
            data_hora="20/11/2026 14:00",
            diagnostico="Consulta de retorno",
            valor_consulta=100
        )

        conflito_detectado = False

        try:
            servico.agendar_consulta(consulta2)
        except ValueError:
            conflito_detectado = True

        assert conflito_detectado, (
            "ERRO: o sistema aceitou duas consultas "
            "para o mesmo médico no mesmo horário."
        )

        print("PASSOU: conflito de agenda impedido.")

        # TESTE 3: mesmo médico em outro horário deve ser aceito
        consulta3 = Consulta(
            id_paciente=2,
            id_medico=1,
            data_hora="20/11/2026 15:00",
            diagnostico="Consulta de retorno",
            valor_consulta=100
        )

        resultado3 = servico.agendar_consulta(consulta3)

        assert resultado3 is not None

        print("PASSOU: mesmo médico em horário diferente.")

        # TESTE 4: outro médico no mesmo horário deve ser aceito
        consulta4 = Consulta(
            id_paciente=2,
            id_medico=2,
            data_hora="20/11/2026 14:00",
            diagnostico="Avaliação ortopédica",
            valor_consulta=200
        )

        resultado4 = servico.agendar_consulta(consulta4)

        assert resultado4 is not None

        print("PASSOU: médicos diferentes no mesmo horário.")

        assert len(repositorio.get_all()) == 3

        print("\nTODOS OS TESTES FORAM CONCLUÍDOS COM SUCESSO!")

        conexao.close()


if __name__ == "__main__":
    executar_testes()
