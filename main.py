
from database.connection import init_db, get_connection

from repositories.sql.medico_sql_repository import MedicoSqlRepository
from repositories.sql.paciente_sql_repository import PacienteSQLRepository
from repositories.sql.consulta_sql_repository import ConsultaSQLRepository

from services.medico_service import MedicoService
from services.paciente_service import PacienteService
from services.consulta_service import ConsultaService

from menu.menu_medicos import menu_medicos
from menu.menu_pacientes import menu_pacientes
from menu.menu_consultas import menu_consultas
from menu.menu_relatorios import menu_relatorios


def main():
    init_db()

    medico_repo = MedicoSqlRepository("vitacare.db")
    paciente_repo = PacienteSQLRepository(get_connection)

    consulta_conexao = get_connection()
    consulta_repo = ConsultaSQLRepository(consulta_conexao)

    medico_service = MedicoService(medico_repo)
    paciente_service = PacienteService(paciente_repo)

    consulta_service = ConsultaService(
        consulta_repo,
        paciente_repo,
        medico_repo
    )

    try:
        while True:
            print("\n" + "=" * 40)
            print("          VITACARE")
            print("=" * 40)
            print("1 - Gerenciar pacientes")
            print("2 - Gerenciar médicos")
            print("3 - Gerenciar consultas")
            print("4 - Relatórios")
            print("0 - Sair")
            print("=" * 40)

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                menu_pacientes(paciente_service)

            elif opcao == "2":
                menu_medicos(medico_service)

            elif opcao == "3":
                menu_consultas(consulta_service)

            elif opcao == "4":
                menu_relatorios(consulta_service)

            elif opcao == "0":
                print("Encerrando o VitaCare. Até logo!")
                break

            else:
                print("Opção inválida!")

    finally:
        consulta_conexao.close()
        medico_repo.close()


if __name__ == "__main__":
    main()
