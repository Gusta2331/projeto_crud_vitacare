
from repositories.sql.medico_sql_repository import MedicoSqlRepository # type: ignore
from services.medico_service import MedicoService
from menu_medicos import menu_medicos # pyright: ignore[reportMissingImports]


def main():
    repositorio = MedicoSqlRepository("vitacare.db")
    servico = MedicoService(repositorio)

    try:
        menu_medicos(servico)
    finally:
        repositorio.close()


if __name__ == "__main__":
    main()
