import sqlite3

from models.medico import Medico


def menu_medicos(service) -> None:
    while True:
        print("\n========== VITACARE ==========")
        print("         MÓDULO MÉDICOS")
        print("==============================")
        print("1. Cadastrar médico")
        print("2. Listar médicos")
        print("3. Atualizar médico")
        print("4. Remover médico")
        print("0. Voltar")

        opcao = input("informe a opção desejada").strip()

        try:
            if opcao == "1":
                nome = input("Nome do médico: ").strip()
                crm = input("CRM: ").strip()
                especialidade = input("Especialidade: ").strip()
                telefone = input("Telefone: ").strip()

                medico = Medico(
                    nome=nome,
                    crm=crm,
                    especialidade=especialidade,
                    telefone=telefone
                  )

                medico = service.save(medico)
                print(f"\nMédico cadastrado com sucesso! "
                        f"ID: {medico.id_medico}")

            elif opcao == "2":
                    medicos = service.get_all()

                    if not medicos:
                     print("\nNenhum médico cadastrado.")
                     continue

                    print("\n========== MÉDICOS CADASTRADOS ==========")

                    for medico in medicos:
                     print(f"\nID: {medico.id_medico}")
                     print(f"Nome: {medico.nome}")
                     print(f"CRM: {medico.crm}")
                     print(f"Especialidade: {medico.especialidade}")
                     print(f"Telefone: {medico.telefone}")
                    
                    print("-----------------------------------------")

            
            elif opcao == "3":
                id_medico = int(input("informe o ID do médico que deseja atualizar"))
                medico_existente = service.find_by_id(id_medico)
                 
                if medico_existente is None:
                 print("\nMédico não encontrado.")
                 continue
           
                print("\nInforme os dados do novo médico:")
                nome = input(f"informe o nome do novo médico:" [{medico_existente.nome}]).strip()
                crm = input(f"CRM [{medico_existente.crm}]: ").strip()
                especialidade = input("Especialidade "f"[{medico_existente.especialidade}]: ").strip()
                telefone = input(f"Telefone [{medico_existente.telefone}]: " ).strip()

                medico = Medico(
                    id_medico=id_medico,
                    nome=nome or medico_existente.nome,
                    crm=crm or medico_existente.crm,
                    especialidade=(especialidade or medico_existente.especialidade),
                    telefone=telefone or medico_existente.telefone
                    )

                atualizado = service.update(medico)

                if atualizado:
                    print("\nMédico atualizado com sucesso!")
                else:
                    print("\nNão foi possível atualizar o médico.")

            elif opcao == "4":
                id_medico = int(
                    input("ID do médico que deseja remover: ")
                )

                medico = service.find_by_id(id_medico)

                if medico is None:
                    print("\nMédico não encontrado.")
                    continue

                confirmacao = input(
                    f"Confirma a remoção de {medico.nome}? (s/n): "
                ).strip().lower()

                if confirmacao == "s":
                    removido = service.delete(id_medico)

                    if removido:
                        print("\nMédico removido com sucesso!")
                    else:
                        print("\nNão foi possível remover o médico.")
                else:
                    print("\nRemoção cancelada.")

            elif opcao == "0":
                print("\nVoltando ao menu principal...")
                break

            else:
                print("\nOpção inválida. Escolha uma opção do menu.")

        except ValueError as erro:
            print(f"\nErro de validação ou entrada: {erro}")

        except sqlite3.IntegrityError:
            print(
                "\nErro: esse CRM já está cadastrado. "
                "Informe um CRM diferente."
            )

        except sqlite3.Error as erro:
            print(f"\nErro no banco de dados: {erro}")

        except (EOFError, KeyboardInterrupt):
            print("\nOperação interrompida. Voltando ao menu.")
            break