from models.consulta import Consulta
def menu_consultas(servico):
    while True:
        print("\n===== VITACARE =====")
        print("MENU DE CONSULTAS")
        print("1 - Agendar consulta")
        print("2 - Listar consultas")
        print("3 - Buscar consulta")
        print("4 - Atualizar consulta")
        print("5 - Excluir consulta")
        print("0 - Voltar")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 0:
            print("Voltando ao menu principal...")
            break

        elif opcao == 1:
            try:
                id_paciente = int(input("ID do paciente: "))
                id_medico = int(input("ID do médico: "))
                data_hora = input("Data e hora da consulta: ")
                valor_consulta = float(input("Valor da consulta: "))

                diagnostico = "Pendente"
            
            except ValueError:
                print("ID ou valor inválido!")
                continue

            consulta = Consulta(
                id_paciente=id_paciente,
                id_medico=id_medico,
                data_hora=data_hora,
                diagnostico=diagnostico,
                valor_consulta=valor_consulta
            )

            try:
                consulta_salva = servico.agendar_consulta(consulta)

                print(f"Consulta agendada com sucesso! ID: {consulta_salva.id_consulta}")

            except ValueError as erro:
                print(f"Erro ao agendar consulta: {erro}")

        elif opcao == 2:
            consultas = servico.listar_consultas()

            if not consultas:
                print("Nenhuma consulta cadastrada.")
            else:
                for consulta in consultas:
                    print(f"\nID: {consulta.id_consulta}")
                    print(f"Paciente: {consulta.id_paciente}")
                    print(f"Médico: {consulta.id_medico}")
                    print(f"Data e hora: {consulta.data_hora}")
                    print(f"Diagnóstico: {consulta.diagnostico}")
                    print(f"Valor: R$ {consulta.valor_consulta:.2f}")

        elif opcao == 3:
            try:
                id_consulta = int(input("Digite o ID da consulta: "))
            
            except ValueError:
                print("ID inválido!")
                continue

            consulta = servico.buscar_consulta(id_consulta)

            if consulta is None:
                print("Consulta não encontrada!")
            else:
                print(f"\nID: {consulta.id_consulta}")
                print(f"Paciente: {consulta.id_paciente}")
                print(f"Médico: {consulta.id_medico}")
                print(f"Data e hora: {consulta.data_hora}")
                print(f"Diagnóstico: {consulta.diagnostico}")
                print(f"Valor: R$ {consulta.valor_consulta:.2f}")

        elif opcao == 4:
           try:
               id_consulta = int(input("ID da consulta que deseja atualizar: "))
           except ValueError:
               print("ID inválido!")
               continue

           consulta = servico.buscar_consulta(id_consulta)

           if consulta is None:
               print("Consulta não encontrada!")
               continue

           while True:
               print("\n===== ATUALIZAR CONSULTA =====")
               print("1 - Alterar paciente")
               print("2 - Alterar médico")
               print("3 - Alterar data e hora")
               print("4 - Alterar diagnóstico")
               print("5 - Alterar valor da consulta")
               print("0 - Voltar")

               try:
                   opcao_atualizar = int(input("Escolha uma opção: "))
               except ValueError:
                    print("Digite apenas números!")
                    continue

               if opcao_atualizar == 0:
                   break

               if opcao_atualizar not in (1, 2, 3, 4, 5):
                   print("Opção inválida!")
                   continue

               # Guardando o valor antigo caso a atualização falhe.
               if opcao_atualizar == 1:
                   campo = "id_paciente"
               elif opcao_atualizar == 2:
                   campo = "id_medico"
               elif opcao_atualizar == 3:
                   campo = "data_hora"
               elif opcao_atualizar == 4:
                   campo = "diagnostico"
               else:
                   campo = "valor_consulta"

               valor_antigo = getattr(consulta, campo)

               try:
                    if opcao_atualizar == 1:
                        novo_valor = int(input("Novo ID do paciente: "))

                    elif opcao_atualizar == 2:
                        novo_valor = int(input("Novo ID do médico: "))

                    elif opcao_atualizar == 3:
                        novo_valor = input("Nova data e hora: ").strip()
                        if not novo_valor:
                            raise ValueError("Data e hora não podem ficar vazias.")

                    elif opcao_atualizar == 4:
                        novo_valor = input("Novo diagnóstico: ").strip()
                        if not novo_valor:
                            raise ValueError("Diagnóstico não pode ficar vazio.")

                    elif opcao_atualizar == 5:
                        novo_valor = float(input("Novo valor da consulta: "))

                    setattr(consulta, campo, novo_valor)

                    atualizado = servico.atualizar_consulta(consulta)

                    if atualizado:
                        print("Consulta atualizada com sucesso!")
                    else:
                        setattr(consulta, campo, valor_antigo)
                        print("Não foi possível atualizar a consulta.")

               except ValueError as erro:
                   setattr(consulta, campo, valor_antigo)
                   print(f"Erro ao atualizar consulta: {erro}")

               except Exception:
                   setattr(consulta, campo, valor_antigo)
                   print("Erro no banco de dados. Atualização não concluída.")
        elif opcao == 5:
            try:
                id_consulta = int(input("ID da consulta que deseja excluir:"))
            
            except ValueError:
                print("ID inválido!")
                continue

            excluida = servico.excluir_consulta(id_consulta)

            if excluida:
                print("Consulta excluída com sucesso!")
            else:
                print("Consulta não encontrada!")


           