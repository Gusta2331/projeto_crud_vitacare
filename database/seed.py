from database.connection import get_connection


def executar_seed():

    connection = get_connection()

    cursor = connection.cursor()

    try:

        print("\n========================================")
        print("       VITACARE - POVOAMENTO SEED")
        print("========================================")


        pacientes = [
            ("Carlos Henrique", "(77) 99911-2233"),
            ("Mariana Oliveira", "(77) 99822-3344"),
            ("João Pedro Santos", "(77) 99733-4455")
        ]

        ids_pacientes = []

        for nome, telefone in pacientes:

            cursor.execute(
                """
                INSERT INTO paciente (
                    nome,
                    telefone
                )
                VALUES (?, ?)
                """,
                (nome, telefone)
            )

            ids_pacientes.append(cursor.lastrowid)

        print("\n3 pacientes cadastrados com sucesso!")


        medicos = [
            ("Roberto Almeida", "Cardiologia"),
            ("Fernanda Costa", "Dermatologia"),
            ("Ricardo Mendes", "Ortopedia")
        ]

        ids_medicos = []

        for nome, especialidade in medicos:

            cursor.execute(
                """
                INSERT INTO medico (
                    nome,
                    especialidade
                )
                VALUES (?, ?)
                """,
                (nome, especialidade)
            )

            ids_medicos.append(cursor.lastrowid)

        print("3 médicos cadastrados com sucesso!")


        consultas = [
            (
                ids_pacientes[0],
                ids_medicos[0],
                "2026-11-01 08:00:00",
                250.00
            ),
            (
                ids_pacientes[1],
                ids_medicos[0],
                "2026-11-01 09:00:00",
                300.00
            ),
            (
                ids_pacientes[2],
                ids_medicos[1],
                "2026-11-02 10:00:00",
                200.00
            ),
            (
                ids_pacientes[0],
                ids_medicos[1],
                "2026-11-02 11:00:00",
                250.00
            ),
            (
                ids_pacientes[1],
                ids_medicos[2],
                "2026-11-03 14:00:00",
                180.00
            ),
            (
                ids_pacientes[2],
                ids_medicos[2],
                "2026-11-03 15:00:00",
                220.00
            )
        ]

        for consulta in consultas:

            cursor.execute(
                """
                INSERT INTO consulta (
                    id_paciente,
                    id_medico,
                    data_consulta,
                    valor_consulta
                )
                VALUES (?, ?, ?, ?)
                """,
                consulta
            )

        print("6 consultas cadastradas com sucesso!")


        connection.commit()

        print("\n========================================")
        print("       SEED EXECUTADO COM SUCESSO!")
        print("========================================")

        print("\nResumo do povoamento:")
        print("Pacientes: 3")
        print("Médicos: 3")
        print("Consultas: 6")

        print("\nTodos os dados foram salvos no SQLite.")

    except Exception as erro:

        connection.rollback()

        print("\nERRO AO EXECUTAR O SEED!")
        print(f"Detalhes: {erro}")

        raise

    finally:

        connection.close()


if __name__ == "__main__":

    executar_seed()