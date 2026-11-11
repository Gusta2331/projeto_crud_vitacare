
def menu_pacientes(servico):
    while True:
        print("\n===== VITACARE =====")
        print("MENU DE PACIENTES")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Buscar paciente")
        print("4 - Atualizar paciente")
        print("5 - Excluir paciente")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break

        elif opcao == "1":
            try:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                data_nascimento = input("Data de nascimento: ")
                telefone = input("Telefone: ")

                paciente = servico.cadastrar(
                    nome, cpf, data_nascimento, telefone
                )
                print(f"Paciente cadastrado! ID: {paciente.id_paciente}")

            except ValueError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Erro ao cadastrar paciente: {erro}")

        elif opcao == "2":
            pacientes = servico.listar_todos()

            if not pacientes:
                print("Nenhum paciente cadastrado.")
            else:
                for paciente in pacientes:
                    print(f"\nID: {paciente.id_paciente}")
                    print(f"Nome: {paciente.nome}")
                    print(f"CPF: {paciente.cpf}")
                    print(f"Nascimento: {paciente.data_nascimento}")
                    print(f"Telefone: {paciente.telefone}")

        elif opcao == "3":
            try:
                id_paciente = int(input("ID do paciente: "))
                paciente = servico.buscar_por_id(id_paciente)

                print(f"\nID: {paciente.id_paciente}")
                print(f"Nome: {paciente.nome}")
                print(f"CPF: {paciente.cpf}")
                print(f"Nascimento: {paciente.data_nascimento}")
                print(f"Telefone: {paciente.telefone}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                id_paciente = int(input("ID do paciente: "))
                paciente = servico.buscar_por_id(id_paciente)

                print("\nInforme os novos dados:")
                nome = input(f"Nome [{paciente.nome}]: ").strip() or paciente.nome
                cpf = input(f"CPF [{paciente.cpf}]: ").strip() or paciente.cpf
                nascimento = input(
                    f"Data de nascimento [{paciente.data_nascimento}]: "
                ).strip() or paciente.data_nascimento
                telefone = input(
                    f"Telefone [{paciente.telefone}]: "
                ).strip() or paciente.telefone

                if servico.atualizar(
                    id_paciente, nome, cpf, nascimento, telefone
                ):
                    print("Paciente atualizado com sucesso!")
                else:
                    print("Não foi possível atualizar o paciente.")

            except ValueError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Erro ao atualizar paciente: {erro}")

        elif opcao == "5":
            try:
                id_paciente = int(input("ID do paciente que deseja excluir: "))

                confirmacao = input(
                    "Confirma a exclusão? (s/n): "
                ).strip().lower()

                if confirmacao == "s":
                    if servico.deletar(id_paciente):
                        print("Paciente excluído com sucesso!")
                    else:
                        print("Não foi possível excluir o paciente.")

            except ValueError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Erro ao excluir paciente: {erro}")

        else:
            print("Opção inválida!")
