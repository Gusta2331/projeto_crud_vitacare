
from models.medico import Medico


def menu_medicos(servico):
    while True:
        print("\n===== VITACARE =====")
        print("MENU DE MÉDICOS")
        print("1 - Cadastrar médico")
        print("2 - Listar médicos")
        print("3 - Buscar médico")
        print("4 - Atualizar médico")
        print("5 - Excluir médico")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break

        elif opcao == "1":
            try:
                nome = input("Nome: ")
                crm = input("CRM: ")
                especialidade = input("Especialidade: ")
                telefone = input("Telefone: ")

                medico = Medico(
                    nome=nome,
                    crm=crm,
                    especialidade=especialidade,
                    telefone=telefone
                )

                medico_salvo = servico.save(medico)
                print(f"Médico cadastrado! ID: {medico_salvo.id_medico}")

            except ValueError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Erro ao cadastrar médico: {erro}")

        elif opcao == "2":
            medicos = servico.get_all()

            if not medicos:
                print("Nenhum médico cadastrado.")
            else:
                for medico in medicos:
                    print(f"\nID: {medico.id_medico}")
                    print(f"Nome: {medico.nome}")
                    print(f"CRM: {medico.crm}")
                    print(f"Especialidade: {medico.especialidade}")
                    print(f"Telefone: {medico.telefone}")

        elif opcao == "3":
            try:
                id_medico = int(input("ID do médico: "))
                medico = servico.find_by_id(id_medico)

                if medico is None:
                    print("Médico não encontrado.")
                else:
                    print(f"\nID: {medico.id_medico}")
                    print(f"Nome: {medico.nome}")
                    print(f"CRM: {medico.crm}")
                    print(f"Especialidade: {medico.especialidade}")
                    print(f"Telefone: {medico.telefone}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                id_medico = int(input("ID do médico: "))
                medico = servico.find_by_id(id_medico)

                if medico is None:
                    print("Médico não encontrado.")
                    continue

                print("\nInforme os novos dados:")
                nome = input(f"Nome [{medico.nome}]: ").strip() or medico.nome
                crm = input(f"CRM [{medico.crm}]: ").strip() or medico.crm
                especialidade = input(
                    f"Especialidade [{medico.especialidade}]: "
                ).strip() or medico.especialidade
                telefone = input(
                    f"Telefone [{medico.telefone}]: "
                ).strip() or medico.telefone

                medico_atualizado = Medico(
                    nome=nome,
                    crm=crm,
                    especialidade=especialidade,
                    telefone=telefone,
                    id_medico=id_medico
                )

                if servico.update(medico_atualizado):
                    print("Médico atualizado com sucesso!")
                else:
                    print("Não foi possível atualizar o médico.")

            except ValueError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Erro ao atualizar médico: {erro}")

        elif opcao == "5":
            try:
                id_medico = int(input("ID do médico que deseja excluir: "))

                confirmacao = input(
                    "Confirma a exclusão? (s/n): "
                ).strip().lower()

                if confirmacao == "s":
                    if servico.delete(id_medico):
                        print("Médico excluído com sucesso!")
                    else:
                        print("Médico não encontrado.")

            except ValueError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Erro ao excluir médico: {erro}")

        else:
            print("Opção inválida!")
